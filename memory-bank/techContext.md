# Technical Context: Live Food Agent Stack

## Technology Stack

### Backend Framework
- **FastAPI**: Modern Python web framework for API development
  - **WebSocket Support**: Native real-time communication
  - **Automatic Documentation**: OpenAPI/Swagger integration
  - **Type Hints**: Full Python typing support
  - **Async/Await**: Non-blocking request handling

### AI/ML Components
- **Google Gemini Live 2.5 Flash Preview**: Primary LLM
  - **Real-time Processing**: Streaming responses
  - **Multi-modal**: Text and audio input/output
  - **Spanish Language**: Native es-ES support
  - **Function Calling**: Tool integration capabilities

- **Google ADK (Agent Development Kit)**:
  - **Agent Framework**: `google.adk.agents.Agent`
  - **Session Management**: `InMemorySessionService`
  - **Tool Integration**: `google.adk.agents.run_config.RunConfig`
  - **Live Streaming**: `LiveRequestQueue` for real-time communication

### Frontend Technologies
- **HTML5**: Semantic markup with modern features
- **CSS3**: Grid/Flexbox layouts, animations, responsive design
- **Vanilla JavaScript**: No framework dependencies
- **Web Audio API**: Real-time audio processing
- **WebSockets**: Bidirectional client-server communication
- **Audio Worklets**: High-performance audio processing

### Audio Processing
- **PCM Format**: Raw audio data streaming
- **Base64 Encoding**: WebSocket-compatible audio transmission
- **Real-time Processing**: Worklet-based audio handling
- **Spanish Voice**: es-ES with "Leda" voice configuration

## Development Environment

### Python Requirements
```python
# Key dependencies from requirements.txt
fastapi                    # Web framework
uvicorn                   # ASGI server
websockets                # WebSocket support
google-genai              # Gemini API integration
python-dotenv            # Environment variable management
pathlib                  # Modern file path handling
asyncio                  # Asynchronous programming
```

### Environment Configuration
```bash
# Required environment variables (.env)
GOOGLE_API_KEY=your_gemini_api_key_here

# Optional configurations
# Development server settings handled by FastAPI defaults
```

### Project Structure
```
live-food-agent/
├── app/                           # Main application
│   ├── main.py                   # FastAPI server & WebSocket handling
│   ├── food/
│   │   ├── agent.py              # Agent configuration
│   │   └── tools/
│   │       ├── prompts.py        # Félix personality & instructions  
│   │       └── tools.py          # Business logic functions
│   └── static/                   # Frontend assets
│       ├── index.html            # Main UI (3-column layout)
│       └── js/
│           ├── app.js            # WebSocket client & UI logic
│           └── audio/            # Audio processing components
├── memory-bank/                   # Project documentation
├── requirements.txt               # Python dependencies
├── setup_venv.sh                 # Environment setup script
└── .env                          # Environment variables
```

## Development Setup

### Quick Start Commands
```bash
# 1. Clone and setup
git clone https://github.com/duboc/live-food-agent.git
cd live-food-agent

# 2. Environment setup
chmod +x setup_venv.sh
./setup_venv.sh

# 3. Configure API key
cp .env.example .env
# Edit .env to add GOOGLE_API_KEY

# 4. Run development server
source venv/bin/activate
cd app
uvicorn main:app --reload

# 5. Access application
open http://localhost:8000
```

### Development Server
- **Host**: `localhost:8000`
- **Hot Reload**: `--reload` flag for development
- **Debug Mode**: FastAPI automatic debugging
- **Console Logging**: Structured logging for all components

## API Endpoints

### Web Interface
- `GET /` → Main application interface (`static/index.html`)
- `GET /static/*` → Static file serving

### WebSocket Connection
- `WebSocket /ws/{session_id}?is_audio={true|false}` → Real-time communication

### REST API (Debug/Utility)
- `GET /debug/pedidos` → View all active orders
- `GET /debug/cardapio` → View complete menu and combos
- `GET /api/pedido/{session_id}` → Get specific session's order

## Configuration Patterns

### Agent Configuration
```python
# app/food/agent.py
root_agent = Agent(
    model="gemini-live-2.5-flash-preview",
    name="ComidaRapidaFantasticaAgent",
    description="Félix, el Amigo del Sabor - Agente de atendimento",
    instruction=top_level_prompt,  # Imported from prompts.py
    tools=[...tool_functions...]   # Imported from tools.py
)
```

### Audio Configuration
```python
# Speech settings for Spanish voice
speech_config = types.SpeechConfig(
    language_code="es-ES",
    voice_config=types.VoiceConfig(
        prebuilt_voice_config=types.PrebuiltVoiceConfig(
            voice_name="Leda"  # Available: Puck, Charon, Kore, Fenrir, Aoede, Leda, Orus, Zephyr
        )
    )
)
```

### WebSocket Message Format
```javascript
// Text message format
{
    "mime_type": "text/plain",
    "data": "message content",
    "role": "user|model"
}

// Audio message format  
{
    "mime_type": "audio/pcm", 
    "data": "base64_encoded_audio_data",
    "role": "user|model"
}
```

## Performance Considerations

### Real-time Requirements
- **WebSocket Latency**: Sub-100ms for text messages
- **Audio Latency**: Target <200ms end-to-end
- **Streaming Response**: Character-by-character text updates
- **Concurrent Sessions**: Multiple users supported via async handling

### Memory Management
- **In-memory State**: Current orders stored in Python dictionary
- **Session Cleanup**: Manual cleanup on order completion
- **Audio Buffering**: Minimal buffering for real-time processing

### Development vs Production
- **Development**: Single-server, in-memory storage, hot reload
- **Production Considerations**: Database integration, load balancing, persistent storage

## Integration Points

### Google Services
- **Gemini API**: Primary AI model integration
- **ADK Framework**: Agent development and management
- **Authentication**: API key-based authentication

### Browser APIs
- **WebSocket API**: Real-time communication
- **Web Audio API**: Audio capture and playback
- **Audio Worklets**: High-performance audio processing
- **MediaDevices API**: Microphone access

### Future Integration Possibilities
- **Payment Processing**: Stripe, PayPal integration
- **Database**: PostgreSQL, MongoDB for persistent storage
- **Analytics**: Order tracking and customer insights
- **Authentication**: User accounts and session management

This technical stack provides a solid foundation for real-time conversational AI with room for scaling and enhancement.
