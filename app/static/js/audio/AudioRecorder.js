/**
 * AudioRecorder for Félix
 * Handles microphone input with volume monitoring and error recovery
 */

import { loadWorkletFromPath, registerWorklet, cleanupWorklets } from './audioworklet-registry.js';

export class AudioRecorder {
  constructor(sampleRate = 16000) {
    this.sampleRate = sampleRate;
    this.stream = null;
    this.audioContext = null;
    this.source = null;
    this.recording = false;
    this.recordingWorklet = null;
    this.vuWorklet = null;
    this.starting = null;
    
    // Event callbacks
    this.onData = null;
    this.onVolume = null;
    this.onError = null;
  }

  /**
   * Convert array buffer to base64
   */
  arrayBufferToBase64(buffer) {
    let binary = '';
    const bytes = new Uint8Array(buffer);
    const len = bytes.byteLength;
    for (let i = 0; i < len; i++) {
      binary += String.fromCharCode(bytes[i]);
    }
    return window.btoa(binary);
  }

  /**
   * Start recording audio
   */
  async start() {
    if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
      throw new Error('El navegador no soporta grabación de audio');
    }

    this.starting = new Promise(async (resolve, reject) => {
      try {
        // Request microphone access
        this.stream = await navigator.mediaDevices.getUserMedia({ 
          audio: {
            channelCount: 1,
            echoCancellation: true,
            noiseSuppression: true,
            autoGainControl: true
          }
        });

        // Create audio context with specified sample rate
        this.audioContext = new AudioContext({ sampleRate: this.sampleRate });
        this.source = this.audioContext.createMediaStreamSource(this.stream);

        // Load and setup recording worklet
        const recordingWorkletUrl = loadWorkletFromPath('./worklets/audio-processing.js');
        await this.audioContext.audioWorklet.addModule(recordingWorkletUrl);
        this.recordingWorklet = new AudioWorkletNode(
          this.audioContext,
          'audio-processing-worklet'
        );

        // Handle audio data from recording worklet
        this.recordingWorklet.port.onmessage = (event) => {
          if (event.data.event === 'chunk') {
            const arrayBuffer = event.data.data.int16arrayBuffer;
            if (arrayBuffer && this.onData) {
              const base64Data = this.arrayBufferToBase64(arrayBuffer);
              this.onData(base64Data);
            }
          }
        };

        // Connect recording worklet
        this.source.connect(this.recordingWorklet);
        registerWorklet(this.audioContext, 'audio-processing-worklet', this.recordingWorklet);

        // Load and setup volume meter worklet
        const vuWorkletUrl = loadWorkletFromPath('./worklets/vol-meter.js');
        await this.audioContext.audioWorklet.addModule(vuWorkletUrl);
        this.vuWorklet = new AudioWorkletNode(this.audioContext, 'vol-meter');

        // Handle volume data
        this.vuWorklet.port.onmessage = (event) => {
          if (typeof event.data.volume === 'number' && this.onVolume) {
            this.onVolume(event.data.volume);
          }
        };

        // Connect volume meter
        this.source.connect(this.vuWorklet);
        registerWorklet(this.audioContext, 'vol-meter', this.vuWorklet);

        this.recording = true;
        resolve();
      } catch (err) {
        // Handle common errors with user-friendly messages
        let errorMessage = 'Error al iniciar grabación: ';
        
        if (err.name === 'NotAllowedError') {
          errorMessage = 'Por favor, permite el acceso al micrófono para hablar con Félix';
        } else if (err.name === 'NotFoundError') {
          errorMessage = 'No se encontró ningún micrófono. Por favor, conecta uno';
        } else if (err.name === 'NotReadableError') {
          errorMessage = 'El micrófono está siendo usado por otra aplicación';
        } else {
          errorMessage += err.message;
        }

        if (this.onError) {
          this.onError(new Error(errorMessage));
        }
        
        reject(err);
      } finally {
        this.starting = null;
      }
    });

    await this.starting;
  }

  /**
   * Stop recording and clean up resources
   */
  stop() {
    const handleStop = () => {
      // Disconnect audio nodes
      if (this.source) {
        this.source.disconnect();
        this.source = null;
      }

      // Stop media stream tracks
      if (this.stream) {
        this.stream.getTracks().forEach(track => track.stop());
        this.stream = null;
      }

      // Close worklet ports
      if (this.recordingWorklet) {
        this.recordingWorklet.port.close();
        this.recordingWorklet.disconnect();
        this.recordingWorklet = null;
      }

      if (this.vuWorklet) {
        this.vuWorklet.port.close();
        this.vuWorklet.disconnect();
        this.vuWorklet = null;
      }

      // Clean up registered worklets and close audio context
      if (this.audioContext) {
        cleanupWorklets(this.audioContext);
        this.audioContext.close().catch(console.error);
        this.audioContext = null;
      }

      this.recording = false;
    };

    // Handle case where stop is called before start completes
    if (this.starting) {
      this.starting.then(handleStop).catch(handleStop);
      return;
    }

    handleStop();
  }

  /**
   * Get current recording state
   */
  isRecording() {
    return this.recording;
  }

  /**
   * Update volume meter settings
   */
  updateVolumeSettings(intervalMs) {
    if (this.vuWorklet) {
      this.vuWorklet.port.postMessage({ updateIntervalInMS: intervalMs });
    }
  }
}
