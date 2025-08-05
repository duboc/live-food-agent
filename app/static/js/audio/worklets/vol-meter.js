/**
 * Volume Meter Worklet for Félix
 * Provides real-time audio level monitoring
 */
class VolMeter extends AudioWorkletProcessor {
  constructor() {
    super();
    
    // Volume tracking
    this.volume = 0;
    this.updateIntervalInMS = 25; // Update every 25ms
    this.nextUpdateFrame = this.updateIntervalInMS;
    
    // Allow dynamic update interval configuration
    this.port.onmessage = event => {
      if (event.data.updateIntervalInMS) {
        this.updateIntervalInMS = event.data.updateIntervalInMS;
      }
    };
  }

  /**
   * Calculate interval in frames based on sample rate
   */
  get intervalInFrames() {
    return (this.updateIntervalInMS / 1000) * sampleRate;
  }

  /**
   * Process audio input and calculate volume levels
   */
  process(inputs) {
    const input = inputs[0];

    if (input.length > 0) {
      const samples = input[0];
      let sum = 0;
      let rms = 0;

      // Calculate RMS (Root Mean Square) for volume level
      for (let i = 0; i < samples.length; ++i) {
        sum += samples[i] * samples[i];
      }

      rms = Math.sqrt(sum / samples.length);
      
      // Smooth volume transitions with decay factor
      // This prevents jumpy volume meters
      this.volume = Math.max(rms, this.volume * 0.7);

      // Check if it's time to send an update
      this.nextUpdateFrame -= samples.length;
      if (this.nextUpdateFrame < 0) {
        this.nextUpdateFrame += this.intervalInFrames;
        
        // Send volume data to main thread
        this.port.postMessage({ 
          volume: this.volume
        });
      }
    }

    // Return true to keep processor alive
    return true;
  }
}

registerProcessor("vol-meter", VolMeter);
