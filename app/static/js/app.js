/**
 * app.js: JS code for the adk-streaming sample app.
 */

/**
 * WebSocket handling
 */

// Global variables
const sessionId = "default"; // Use consistent session ID
const ws_url = "ws://" + window.location.host + "/ws/" + sessionId;
let websocket = null;
let is_audio = false;
let currentMessageId = null; // Track the current message ID during a conversation turn

// Get DOM elements
const messageForm = document.getElementById("messageForm");
const messageInput = document.getElementById("message");
const messagesDiv = document.getElementById("messages");
const statusDot = document.getElementById("status-dot");
const connectionStatus = document.getElementById("connection-status");
const typingIndicator = document.getElementById("typing-indicator");
const startAudioButton = document.getElementById("startAudioButton");
const stopAudioButton = document.getElementById("stopAudioButton");
const recordingContainer = document.getElementById("recording-container");

// WebSocket handlers
function connectWebsocket() {
  // Connect websocket
  const wsUrl = ws_url + "?is_audio=" + is_audio;
  websocket = new WebSocket(wsUrl);

  // Handle connection open
  websocket.onopen = function () {
    // Connection opened messages
    console.log("WebSocket connection opened.");
    connectionStatus.textContent = "Connected";
    statusDot.classList.add("connected");

    // Enable the Send button
    document.getElementById("sendButton").disabled = false;
    addSubmitHandler();
    
    // Call custom onOpen handler if defined
    if (typeof window.onWebSocketOpen === 'function') {
      window.onWebSocketOpen();
    }
  };

  // Handle incoming messages
  websocket.onmessage = function (event) {
    // Parse the incoming message
    const message_from_server = JSON.parse(event.data);
    console.log("[AGENT TO CLIENT] ", message_from_server);

    // Show typing indicator for first message in a response sequence,
    // but not for turn_complete messages
    if (
      !message_from_server.turn_complete &&
      (message_from_server.mime_type === "text/plain" ||
        message_from_server.mime_type === "audio/pcm")
    ) {
      typingIndicator.classList.add("visible");
    }

    // Check if the turn is complete
    if (
      message_from_server.turn_complete &&
      message_from_server.turn_complete === true
    ) {
      // Reset currentMessageId to ensure the next message gets a new element
      currentMessageId = null;
      typingIndicator.classList.remove("visible");
      
      // Mark audio stream as complete
      if (audioStreamer) {
        audioStreamer.complete();
      }
      
      return;
    }

    // If it's audio, play it
    if (message_from_server.mime_type === "audio/pcm" && audioStreamer) {
      // Add audio data to streamer
      audioStreamer.addPCM16(message_from_server.data);

      // If we have an existing message element for this turn, add audio icon if needed
      if (currentMessageId) {
        const messageElem = document.getElementById(currentMessageId);
        if (
          messageElem &&
          !messageElem.querySelector(".audio-icon") &&
          is_audio
        ) {
          const audioIcon = document.createElement("span");
          audioIcon.className = "audio-icon";
          messageElem.prepend(audioIcon);
        }
      }
    }

    // Handle text messages
    if (message_from_server.mime_type === "text/plain") {
      // Hide typing indicator
      typingIndicator.classList.remove("visible");

      const role = message_from_server.role || "model";

      // If we already have a message element for this turn, append to it
      if (currentMessageId && role === "model") {
        const existingMessage = document.getElementById(currentMessageId);
        if (existingMessage) {
          // Append the text without adding extra spaces
          // Use a span element to maintain proper text flow
          const textNode = document.createTextNode(message_from_server.data);
          existingMessage.appendChild(textNode);

          // Scroll to the bottom
          messagesDiv.scrollTop = messagesDiv.scrollHeight;
          return;
        }
      }

      // Create a new message element if it's a new turn or user message
      const messageId = Math.random().toString(36).substring(7);
      const messageElem = document.createElement("p");
      messageElem.id = messageId;

      // Set class based on role
      messageElem.className =
        role === "user" ? "user-message" : "agent-message";

      // Add audio icon for model messages if audio is enabled
      if (is_audio && role === "model") {
        const audioIcon = document.createElement("span");
        audioIcon.className = "audio-icon";
        messageElem.appendChild(audioIcon);
      }

      // Add the text content
      messageElem.appendChild(
        document.createTextNode(message_from_server.data)
      );

      // Add the message to the DOM
      messagesDiv.appendChild(messageElem);

      // Remember the ID of this message for subsequent responses in this turn
      if (role === "model") {
        currentMessageId = messageId;
      }

      // Scroll to the bottom
      messagesDiv.scrollTop = messagesDiv.scrollHeight;
    }
    
    // Call custom message handler if defined
    if (typeof window.handleWebSocketMessage === 'function') {
      window.handleWebSocketMessage(message_from_server);
    }
  };

  // Handle connection close
  websocket.onclose = function () {
    console.log("WebSocket connection closed.");
    document.getElementById("sendButton").disabled = true;
    connectionStatus.textContent = "Disconnected. Reconnecting...";
    statusDot.classList.remove("connected");
    typingIndicator.classList.remove("visible");
    
    // Call custom onClose handler if defined
    if (typeof window.onWebSocketClose === 'function') {
      window.onWebSocketClose();
    }
    
    setTimeout(function () {
      console.log("Reconnecting...");
      connectWebsocket();
    }, 5000);
  };

  websocket.onerror = function (e) {
    console.log("WebSocket error: ", e);
    connectionStatus.textContent = "Connection error";
    statusDot.classList.remove("connected");
    typingIndicator.classList.remove("visible");
  };
}
connectWebsocket();

// Add submit handler to the form
function addSubmitHandler() {
  messageForm.onsubmit = function (e) {
    e.preventDefault();
    const message = messageInput.value;
    if (message) {
      const p = document.createElement("p");
      p.textContent = message;
      p.className = "user-message";
      messagesDiv.appendChild(p);
      messageInput.value = "";

      // Show typing indicator after sending message
      typingIndicator.classList.add("visible");

      sendMessage({
        mime_type: "text/plain",
        data: message,
        role: "user",
      });
      console.log("[CLIENT TO AGENT] " + message);
      // Scroll down to the bottom of the messagesDiv
      messagesDiv.scrollTop = messagesDiv.scrollHeight;
    }
    return false;
  };
}

// Send a message to the server as a JSON string
function sendMessage(message) {
  if (websocket && websocket.readyState == WebSocket.OPEN) {
    const messageJson = JSON.stringify(message);
    websocket.send(messageJson);
  }
}

// Decode Base64 data to Array
function base64ToArray(base64) {
  const binaryString = window.atob(base64);
  const len = binaryString.length;
  const bytes = new Uint8Array(len);
  for (let i = 0; i < len; i++) {
    bytes[i] = binaryString.charCodeAt(i);
  }
  return bytes.buffer;
}

/**
 * Audio handling
 */

// Import the new audio components
import { AudioRecorder } from "./audio/AudioRecorder.js";
import { AudioStreamer } from "./audio/AudioStreamer.js";

// Audio component instances
let audioRecorder = null;
let audioStreamer = null;
let isRecording = false;

// Volume visualization elements (will be created dynamically)
let recordingVolumeBar = null;
let playbackVolumeBar = null;

// Create volume visualization UI
function createVolumeVisualization() {
  // Create container for volume meters
  const volumeContainer = document.createElement("div");
  volumeContainer.id = "volume-meters";
  volumeContainer.style.cssText = `
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: white;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
    display: none;
    flex-direction: column;
    gap: 10px;
    min-width: 200px;
  `;

  // Recording volume meter
  const recordingMeter = document.createElement("div");
  recordingMeter.innerHTML = `
    <div style="font-size: 12px; font-weight: 600; color: #FF4444; margin-bottom: 5px;">
      🎤 Micrófono
    </div>
    <div style="background: #eee; height: 6px; border-radius: 3px; overflow: hidden;">
      <div id="recording-volume-bar" style="height: 100%; background: #FF4444; width: 0%; transition: width 0.1s ease;"></div>
    </div>
  `;

  // Playback volume meter
  const playbackMeter = document.createElement("div");
  playbackMeter.innerHTML = `
    <div style="font-size: 12px; font-weight: 600; color: #22CC44; margin-bottom: 5px;">
      🔊 Félix
    </div>
    <div style="background: #eee; height: 6px; border-radius: 3px; overflow: hidden;">
      <div id="playback-volume-bar" style="height: 100%; background: #22CC44; width: 0%; transition: width 0.1s ease;"></div>
    </div>
  `;

  volumeContainer.appendChild(recordingMeter);
  volumeContainer.appendChild(playbackMeter);
  document.body.appendChild(volumeContainer);

  // Get references to volume bars
  recordingVolumeBar = document.getElementById("recording-volume-bar");
  playbackVolumeBar = document.getElementById("playback-volume-bar");

  return volumeContainer;
}

// Initialize audio components
async function startAudio() {
  try {
    // Create volume visualization if not exists
    const volumeMeters = document.getElementById("volume-meters") || createVolumeVisualization();
    volumeMeters.style.display = "flex";

    // Initialize audio streamer (for playback)
    audioStreamer = new AudioStreamer();
    await audioStreamer.resume();

    // Set up playback volume monitoring
    audioStreamer.onVolume = (volume) => {
      if (playbackVolumeBar) {
        const percentage = Math.min(100, volume * 200); // Scale for visibility
        playbackVolumeBar.style.width = percentage + "%";
      }
    };

    audioStreamer.onError = (error) => {
      console.error("Audio playback error:", error);
      showError("Error en reproducción de audio");
    };

    // Initialize audio recorder
    audioRecorder = new AudioRecorder(16000); // 16kHz for ADK

    // Set up recording callbacks
    audioRecorder.onData = (base64Data) => {
      if (isRecording) {
        sendMessage({
          mime_type: "audio/pcm",
          data: base64Data,
        });
      }
    };

    audioRecorder.onVolume = (volume) => {
      if (recordingVolumeBar) {
        const percentage = Math.min(100, volume * 200); // Scale for visibility
        recordingVolumeBar.style.width = percentage + "%";
      }
    };

    audioRecorder.onError = (error) => {
      console.error("Recording error:", error);
      showError(error.message);
      stopAudio();
    };

    // Start recording
    await audioRecorder.start();
    isRecording = true;

    console.log("Audio system initialized successfully");
  } catch (error) {
    console.error("Failed to start audio:", error);
    showError("Error al iniciar el audio: " + error.message);
    throw error;
  }
}

// Stop audio components
function stopAudio() {
  isRecording = false;

  // Stop and clean up recorder
  if (audioRecorder) {
    audioRecorder.stop();
    audioRecorder = null;
  }

  // Stop and clean up streamer
  if (audioStreamer) {
    audioStreamer.destroy();
    audioStreamer = null;
  }

  // Hide volume meters
  const volumeMeters = document.getElementById("volume-meters");
  if (volumeMeters) {
    volumeMeters.style.display = "none";
  }

  console.log("Audio system stopped");
}

// Show error message to user
function showError(message) {
  const errorDiv = document.createElement("div");
  errorDiv.style.cssText = `
    position: fixed;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    background: #FF4444;
    color: white;
    padding: 15px 25px;
    border-radius: 8px;
    box-shadow: 0 4px 15px rgba(255, 68, 68, 0.3);
    z-index: 1000;
    animation: slideIn 0.3s ease-out;
  `;
  errorDiv.textContent = message;
  document.body.appendChild(errorDiv);

  setTimeout(() => {
    errorDiv.style.animation = "slideOut 0.3s ease-out";
    setTimeout(() => errorDiv.remove(), 300);
  }, 5000);
}

// Start the audio only when the user clicked the button
// (due to the gesture requirement for the Web Audio API)
startAudioButton.addEventListener("click", () => {
  startAudioButton.disabled = true;
  startAudioButton.textContent = "Voice Enabled";
  startAudioButton.style.display = "none";
  stopAudioButton.style.display = "inline-block";
  recordingContainer.style.display = "flex";
  startAudio();
  is_audio = true;

  // Add class to messages container to enable audio styling
  messagesDiv.classList.add("audio-enabled");

  connectWebsocket(); // reconnect with the audio mode
});

// Stop audio recording when stop button is clicked
stopAudioButton.addEventListener("click", () => {
  stopAudio();
  stopAudioButton.style.display = "none";
  startAudioButton.style.display = "inline-block";
  startAudioButton.disabled = false;
  startAudioButton.textContent = "Enable Voice";
  recordingContainer.style.display = "none";

  // Remove audio styling class
  messagesDiv.classList.remove("audio-enabled");

  // Reconnect without audio mode
  is_audio = false;

  // Only reconnect if the connection is still open
  if (websocket && websocket.readyState === WebSocket.OPEN) {
    websocket.close();
    // The onclose handler will trigger reconnection
  }
});

// Add CSS animations for error messages and volume meters
const style = document.createElement('style');
style.textContent = `
  @keyframes slideIn {
    from {
      opacity: 0;
      transform: translate(-50%, -20px);
    }
    to {
      opacity: 1;
      transform: translate(-50%, 0);
    }
  }
  
  @keyframes slideOut {
    from {
      opacity: 1;
      transform: translate(-50%, 0);
    }
    to {
      opacity: 0;
      transform: translate(-50%, -20px);
    }
  }
  
  /* Audio volume animations */
  @keyframes pulse-audio {
    0%, 100% {
      opacity: 0.8;
    }
    50% {
      opacity: 1;
    }
  }
  
  /* Improved audio icon animation when speaking */
  .audio-icon {
    animation: pulse-audio 1.5s infinite;
  }
`;
document.head.appendChild(style);
