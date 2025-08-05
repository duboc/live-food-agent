# Audio Settings Implementation Plan - Phase 2

## 🎯 Overview
Implement user-configurable audio settings for Félix, including voice selection, audio quality controls, and accessibility features.

## 🏗️ Architecture

### Frontend Components

```
app/static/
├── js/
│   ├── audio/
│   │   ├── AudioSettings.js       # Settings manager class
│   │   ├── VoicePreview.js        # Voice preview functionality
│   │   └── TranscriptionDisplay.js # Real-time transcription
│   └── components/
│       ├── SettingsModal.js       # Settings UI component
│       └── AudioControls.js       # Audio control widgets
├── css/
│   └── audio-settings.css         # Settings UI styles
└── index.html                     # Updated with settings button
```

### Backend Endpoints

```python
# app/main.py additions
@app.post("/api/voice-preview")    # Generate voice preview
@app.post("/api/voice-settings")   # Update voice configuration
@app.get("/api/available-voices")  # Get list of available voices
```

## 📋 Implementation Tasks

### 1. Voice Selection Panel

#### A. Create Settings Modal UI
```html
<!-- Settings Modal Structure -->
<div id="settings-modal" class="modal">
  <div class="modal-content">
    <h2>⚙️ Configuración de Audio</h2>
    
    <!-- Voice Selection -->
    <div class="setting-group">
      <label>Voz de Félix:</label>
      <select id="voice-select">
        <option value="Leda">Leda (Amigable)</option>
        <option value="Puck">Puck (Enérgico)</option>
        <option value="Charon">Charon (Profundo)</option>
        <option value="Kore">Kore (Neutro)</option>
        <option value="Fenrir">Fenrir (Fuerte)</option>
        <option value="Aoede">Aoede (Melódico)</option>
        <option value="Orus">Orus (Autoritario)</option>
        <option value="Zephyr">Zephyr (Suave)</option>
      </select>
      <button id="preview-voice">🔊 Escuchar</button>
    </div>
  </div>
</div>
```

#### B. AudioSettings.js Class
```javascript
export class AudioSettings {
  constructor() {
    this.settings = this.loadSettings();
    this.observers = [];
  }

  loadSettings() {
    const defaults = {
      voice: {
        name: "Leda",
        speed: 1.0,
        language: "es-ES"
      },
      audio: {
        micSensitivity: 0.7,
        playbackVolume: 0.8,
        quality: "high",
        pushToTalk: false,
        showTranscription: false
      }
    };
    
    const saved = localStorage.getItem('felixAudioSettings');
    return saved ? { ...defaults, ...JSON.parse(saved) } : defaults;
  }

  saveSettings() {
    localStorage.setItem('felixAudioSettings', JSON.stringify(this.settings));
    this.notifyObservers();
  }

  // Observer pattern for reactive updates
  subscribe(callback) {
    this.observers.push(callback);
  }

  notifyObservers() {
    this.observers.forEach(cb => cb(this.settings));
  }
}
```

#### C. Voice Preview Implementation
```javascript
export class VoicePreview {
  constructor(apiEndpoint) {
    this.apiEndpoint = apiEndpoint;
    this.previewAudio = null;
  }

  async previewVoice(voiceName, text = "¡Hola! Soy Félix, tu amigo del sabor.") {
    try {
      const response = await fetch('/api/voice-preview', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ voice: voiceName, text })
      });
      
      const audioData = await response.json();
      await this.playPreview(audioData.audio);
    } catch (error) {
      console.error('Voice preview error:', error);
    }
  }

  async playPreview(base64Audio) {
    // Use existing AudioStreamer for preview
    const streamer = new AudioStreamer();
    await streamer.resume();
    streamer.addPCM16(base64Audio);
  }
}
```

### 2. Audio Quality Settings

#### A. Microphone Sensitivity Control
```javascript
// Add to AudioRecorder.js
setSensitivity(level) {
  // level: 0.0 to 1.0
  if (this.source && this.audioContext) {
    const gainNode = this.audioContext.createGain();
    gainNode.gain.value = level;
    
    // Reconnect with gain
    this.source.disconnect();
    this.source.connect(gainNode);
    gainNode.connect(this.recordingWorklet);
  }
}
```

#### B. Playback Volume Control
```javascript
// Already implemented in AudioStreamer.js
audioStreamer.setVolume(0.8); // 0.0 to 1.0
```

#### C. Audio Quality Preferences
```javascript
const qualityProfiles = {
  low: {
    sampleRate: 8000,
    bufferSize: 512,
    bitrate: "8k"
  },
  medium: {
    sampleRate: 16000,
    bufferSize: 1024,
    bitrate: "16k"
  },
  high: {
    sampleRate: 24000,
    bufferSize: 2048,
    bitrate: "24k"
  }
};
```

### 3. Accessibility Features

#### A. Push-to-Talk Implementation
```javascript
export class PushToTalkHandler {
  constructor(audioRecorder) {
    this.audioRecorder = audioRecorder;
    this.isKeyPressed = false;
    this.hotkey = 'Space'; // Default hotkey
    
    this.setupListeners();
  }

  setupListeners() {
    document.addEventListener('keydown', (e) => {
      if (e.code === this.hotkey && !this.isKeyPressed) {
        this.isKeyPressed = true;
        this.startRecording();
      }
    });
    
    document.addEventListener('keyup', (e) => {
      if (e.code === this.hotkey) {
        this.isKeyPressed = false;
        this.stopRecording();
      }
    });
  }

  startRecording() {
    this.audioRecorder.start();
    this.showPTTIndicator();
  }

  stopRecording() {
    this.audioRecorder.stop();
    this.hidePTTIndicator();
  }
}
```

#### B. Visual Transcription Display
```javascript
export class TranscriptionDisplay {
  constructor(containerElement) {
    this.container = containerElement;
    this.currentTranscript = '';
    this.isVisible = false;
  }

  show() {
    this.container.style.display = 'block';
    this.isVisible = true;
  }

  hide() {
    this.container.style.display = 'none';
    this.isVisible = false;
  }

  updateTranscript(text, isFinal = false) {
    if (!this.isVisible) return;
    
    const transcriptElement = document.createElement('div');
    transcriptElement.className = isFinal ? 'transcript-final' : 'transcript-interim';
    transcriptElement.textContent = text;
    
    this.container.appendChild(transcriptElement);
    this.container.scrollTop = this.container.scrollHeight;
  }
}
```

## 🎨 UI Design Mockup

### Settings Modal Design
```css
.settings-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: none;
  z-index: 1000;
}

.modal-content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: white;
  padding: 30px;
  border-radius: 16px;
  max-width: 600px;
  width: 90%;
  max-height: 80vh;
  overflow-y: auto;
}

.setting-group {
  margin-bottom: 25px;
  padding: 20px;
  background: #f8f8f8;
  border-radius: 12px;
}

.slider-control {
  display: flex;
  align-items: center;
  gap: 15px;
}

.slider {
  flex: 1;
  -webkit-appearance: none;
  height: 6px;
  border-radius: 3px;
  background: #ddd;
  outline: none;
}

.slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: var(--primary-red);
  cursor: pointer;
}

.toggle-switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
}

.toggle-switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.toggle-slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  transition: .4s;
  border-radius: 34px;
}

.toggle-slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  transition: .4s;
  border-radius: 50%;
}

input:checked + .toggle-slider {
  background-color: var(--green-accent);
}

input:checked + .toggle-slider:before {
  transform: translateX(26px);
}
```

## 🔄 Backend Integration

### Voice Configuration Endpoint
```python
@app.post("/api/voice-settings")
async def update_voice_settings(settings: dict):
    """Update voice configuration for a session"""
    voice_name = settings.get("voice", "Leda")
    speed = settings.get("speed", 1.0)
    
    # Store in session
    session_voice_config[session_id] = {
        "voice_name": voice_name,
        "speed": speed
    }
    
    return {"success": True}

@app.post("/api/voice-preview")
async def generate_voice_preview(request: dict):
    """Generate a preview audio clip with specified voice"""
    voice_name = request.get("voice", "Leda")
    text = request.get("text", "¡Hola! Soy Félix, tu amigo del sabor.")
    
    # Generate preview using ADK
    preview_audio = await generate_preview_audio(voice_name, text)
    
    return {
        "audio": base64.b64encode(preview_audio).decode(),
        "voice": voice_name
    }
```

### Modified Session Initialization
```python
def start_agent_session(session_id, is_audio=False, voice_settings=None):
    """Starts an agent session with configurable voice"""
    
    # Get voice settings from request or use defaults
    voice_name = "Leda"
    speed = 1.0
    
    if voice_settings:
        voice_name = voice_settings.get("voice", "Leda")
        speed = voice_settings.get("speed", 1.0)
    
    # Create speech config with selected voice
    speech_config = types.SpeechConfig(
        language_code="es-ES",
        voice_config=types.VoiceConfig(
            prebuilt_voice_config=types.PrebuiltVoiceConfig(
                voice_name=voice_name
            )
        )
    )
    
    # Apply speed adjustment if needed
    if speed != 1.0:
        config["speaking_rate"] = speed
```

## 📱 Mobile Considerations

1. **Touch-friendly controls**
   - Large tap targets (minimum 44x44px)
   - Swipe gestures for volume control
   - Long-press for push-to-talk on mobile

2. **Responsive design**
   - Settings modal adapts to screen size
   - Horizontal sliders stack vertically on mobile
   - Simplified controls for small screens

3. **Performance optimizations**
   - Lazy load settings components
   - Debounce slider changes
   - Minimize localStorage writes

## 🧪 Testing Plan

1. **Voice Selection**
   - Test all 8 voice options
   - Verify preview functionality
   - Check persistence across sessions

2. **Audio Controls**
   - Test sensitivity range (0-100%)
   - Verify volume changes
   - Test quality presets

3. **Accessibility**
   - Test push-to-talk with keyboard
   - Verify transcription display
   - Screen reader compatibility

4. **Cross-browser**
   - Chrome, Firefox, Safari, Edge
   - Mobile browsers (iOS Safari, Chrome)
   - Different screen sizes

## 📅 Implementation Timeline

- **Day 1**: Settings UI and modal (4 hours)
- **Day 2**: Voice selection and preview (6 hours)
- **Day 3**: Audio quality controls (4 hours)
- **Day 4**: Accessibility features (6 hours)
- **Day 5**: Backend integration and testing (4 hours)

**Total**: ~24 hours of development

## 🚀 Next Steps

1. Review and approve the plan
2. Create the settings UI components
3. Implement voice preview functionality
4. Add audio quality controls
5. Implement accessibility features
6. Integrate with backend
7. Test across devices and browsers
