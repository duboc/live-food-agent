/**
 * AudioStreamer for Félix
 * Handles audio playback with buffering and volume monitoring
 */

import { loadWorkletFromPath, registerWorklet, cleanupWorklets } from './audioworklet-registry.js';

export class AudioStreamer {
  constructor(context = null) {
    // Use provided context or create new one at 24kHz for ADK compatibility
    this.context = context || new AudioContext({ sampleRate: 24000 });
    this.sampleRate = this.context.sampleRate;
    
    // Audio buffer management
    this.bufferSize = 7680; // ~320ms at 24kHz
    this.audioQueue = [];
    this.isPlaying = false;
    this.isStreamComplete = false;
    this.checkInterval = null;
    this.scheduledTime = 0;
    this.initialBufferTime = 0.1; // 100ms initial buffer
    
    // Audio nodes
    this.gainNode = this.context.createGain();
    this.gainNode.connect(this.context.destination);
    this.endOfQueueAudioSource = null;
    
    // Event callbacks
    this.onComplete = null;
    this.onVolume = null;
    this.onError = null;
    
    // Volume meter
    this.vuWorklet = null;
    this.setupVolumeMonitoring();
  }

  /**
   * Setup volume monitoring
   */
  async setupVolumeMonitoring() {
    try {
      const vuWorkletUrl = loadWorkletFromPath('./worklets/vol-meter.js');
      await this.context.audioWorklet.addModule(vuWorkletUrl);
      this.vuWorklet = new AudioWorkletNode(this.context, 'vol-meter');
      
      // Handle volume updates
      this.vuWorklet.port.onmessage = (event) => {
        if (typeof event.data.volume === 'number' && this.onVolume) {
          this.onVolume(event.data.volume);
        }
      };
      
      // Don't connect volume meter to destination directly
      // It will be connected in the audio chain
      registerWorklet(this.context, 'vol-meter', this.vuWorklet);
    } catch (err) {
      console.error('Error setting up volume monitoring:', err);
    }
  }

  /**
   * Convert base64 to array buffer
   */
  base64ToArrayBuffer(base64) {
    const binaryString = window.atob(base64);
    const len = binaryString.length;
    const bytes = new Uint8Array(len);
    for (let i = 0; i < len; i++) {
      bytes[i] = binaryString.charCodeAt(i);
    }
    return bytes.buffer;
  }

  /**
   * Process PCM16 chunk to Float32Array
   */
  processPCM16Chunk(chunk) {
    // Ensure we have an ArrayBuffer
    const arrayBuffer = chunk instanceof ArrayBuffer ? chunk : chunk.buffer;
    const float32Array = new Float32Array(arrayBuffer.byteLength / 2);
    const dataView = new DataView(arrayBuffer);

    for (let i = 0; i < float32Array.length; i++) {
      try {
        const int16 = dataView.getInt16(i * 2, true);
        float32Array[i] = int16 / 32768;
      } catch (e) {
        console.error('Error processing audio chunk:', e);
        if (this.onError) {
          this.onError(e);
        }
      }
    }
    return float32Array;
  }

  /**
   * Add PCM16 audio data (base64 encoded)
   */
  addPCM16(base64Data) {
    // Reset stream complete flag when new data arrives
    this.isStreamComplete = false;
    
    // Convert base64 to array buffer
    const arrayBuffer = this.base64ToArrayBuffer(base64Data);
    
    // Process to Float32
    let processingBuffer = this.processPCM16Chunk(arrayBuffer);
    
    // Queue audio in chunks
    while (processingBuffer.length >= this.bufferSize) {
      const buffer = processingBuffer.slice(0, this.bufferSize);
      this.audioQueue.push(buffer);
      processingBuffer = processingBuffer.slice(this.bufferSize);
    }
    
    // Queue remaining data
    if (processingBuffer.length > 0) {
      this.audioQueue.push(processingBuffer);
    }
    
    // Start playing if not already
    if (!this.isPlaying) {
      this.isPlaying = true;
      this.scheduledTime = this.context.currentTime + this.initialBufferTime;
      this.scheduleNextBuffer();
    }
  }

  /**
   * Create audio buffer from Float32Array
   */
  createAudioBuffer(audioData) {
    const audioBuffer = this.context.createBuffer(
      1, // mono
      audioData.length,
      this.sampleRate
    );
    audioBuffer.getChannelData(0).set(audioData);
    return audioBuffer;
  }

  /**
   * Schedule next audio buffer for playback
   */
  scheduleNextBuffer() {
    const SCHEDULE_AHEAD_TIME = 0.2; // Schedule 200ms ahead

    while (
      this.audioQueue.length > 0 &&
      this.scheduledTime < this.context.currentTime + SCHEDULE_AHEAD_TIME
    ) {
      const audioData = this.audioQueue.shift();
      const audioBuffer = this.createAudioBuffer(audioData);
      const source = this.context.createBufferSource();

      // Track end of queue for completion callback
      if (this.audioQueue.length === 0) {
        if (this.endOfQueueAudioSource) {
          this.endOfQueueAudioSource.onended = null;
        }
        this.endOfQueueAudioSource = source;
        source.onended = () => {
          if (
            !this.audioQueue.length &&
            this.endOfQueueAudioSource === source
          ) {
            this.endOfQueueAudioSource = null;
            if (this.onComplete) {
              this.onComplete();
            }
          }
        };
      }

      // Connect audio chain
      source.buffer = audioBuffer;
      source.connect(this.gainNode);
      
      // Also connect to volume meter for monitoring (parallel connection)
      if (this.vuWorklet) {
        source.connect(this.vuWorklet);
      }

      // Schedule playback
      const startTime = Math.max(this.scheduledTime, this.context.currentTime);
      source.start(startTime);
      this.scheduledTime = startTime + audioBuffer.duration;
    }

    // Handle queue management
    if (this.audioQueue.length === 0) {
      if (this.isStreamComplete) {
        this.isPlaying = false;
        if (this.checkInterval) {
          clearInterval(this.checkInterval);
          this.checkInterval = null;
        }
      } else {
        // Check for more data periodically
        if (!this.checkInterval) {
          this.checkInterval = setInterval(() => {
            if (this.audioQueue.length > 0) {
              this.scheduleNextBuffer();
            }
          }, 100);
        }
      }
    } else {
      // Schedule next check
      const nextCheckTime =
        (this.scheduledTime - this.context.currentTime) * 1000;
      setTimeout(
        () => this.scheduleNextBuffer(),
        Math.max(0, nextCheckTime - 50)
      );
    }
  }

  /**
   * Stop audio playback
   */
  stop() {
    this.isPlaying = false;
    this.isStreamComplete = true;
    this.audioQueue = [];
    this.scheduledTime = this.context.currentTime;

    if (this.checkInterval) {
      clearInterval(this.checkInterval);
      this.checkInterval = null;
    }

    // Fade out gracefully
    this.gainNode.gain.linearRampToValueAtTime(
      0,
      this.context.currentTime + 0.1
    );

    // Reset gain after fade
    setTimeout(() => {
      this.gainNode.disconnect();
      this.gainNode = this.context.createGain();
      this.gainNode.connect(this.context.destination);
    }, 200);
  }

  /**
   * Resume audio context if suspended
   */
  async resume() {
    if (this.context.state === 'suspended') {
      await this.context.resume();
    }
    this.isStreamComplete = false;
    this.scheduledTime = this.context.currentTime + this.initialBufferTime;
    this.gainNode.gain.setValueAtTime(1, this.context.currentTime);
  }

  /**
   * Mark stream as complete
   */
  complete() {
    this.isStreamComplete = true;
    if (this.onComplete && this.audioQueue.length === 0) {
      this.onComplete();
    }
  }

  /**
   * Set playback volume
   */
  setVolume(value) {
    const clampedValue = Math.max(0, Math.min(1, value));
    this.gainNode.gain.setValueAtTime(clampedValue, this.context.currentTime);
  }

  /**
   * Get current playback state
   */
  isActive() {
    return this.isPlaying && !this.isStreamComplete;
  }

  /**
   * Clean up resources
   */
  destroy() {
    this.stop();
    
    if (this.vuWorklet) {
      this.vuWorklet.port.close();
      this.vuWorklet.disconnect();
      this.vuWorklet = null;
    }
    
    if (this.context.state !== 'closed') {
      cleanupWorklets(this.context);
      // Don't close context if it was provided externally
      if (!this.externalContext) {
        this.context.close().catch(console.error);
      }
    }
  }
}
