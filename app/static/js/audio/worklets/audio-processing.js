/**
 * Audio Processing Worklet for Félix
 * Handles PCM audio recording with proper buffering
 */
class AudioProcessingWorklet extends AudioWorkletProcessor {
  constructor() {
    super();
    
    // Buffer configuration
    // Send audio chunks every 2048 samples (128ms at 16kHz)
    this.buffer = new Int16Array(2048);
    this.bufferWriteIndex = 0;
    this.hasAudio = false;
  }

  /**
   * Process audio input
   * @param inputs Float32Array[][] [input#][channel#][sample#]
   * @param outputs Float32Array[][]
   */
  process(inputs) {
    if (inputs[0].length) {
      const channel0 = inputs[0][0];
      this.processChunk(channel0);
    }
    return true;
  }

  /**
   * Send buffered audio and clear buffer
   */
  sendAndClearBuffer() {
    this.port.postMessage({
      event: "chunk",
      data: {
        int16arrayBuffer: this.buffer.slice(0, this.bufferWriteIndex).buffer,
      },
    });
    this.bufferWriteIndex = 0;
  }

  /**
   * Process audio chunk and convert to Int16
   * @param float32Array Input audio data
   */
  processChunk(float32Array) {
    const length = float32Array.length;
    
    for (let i = 0; i < length; i++) {
      // Convert float32 (-1 to 1) to int16 (-32768 to 32767)
      const int16Value = Math.max(-32768, Math.min(32767, float32Array[i] * 32768));
      this.buffer[this.bufferWriteIndex++] = int16Value;
      
      // Send buffer when full
      if (this.bufferWriteIndex >= this.buffer.length) {
        this.sendAndClearBuffer();
      }
    }

    // Send remaining data if buffer has content
    if (this.bufferWriteIndex >= this.buffer.length) {
      this.sendAndClearBuffer();
    }
  }
}

registerProcessor("audio-processing-worklet", AudioProcessingWorklet);
