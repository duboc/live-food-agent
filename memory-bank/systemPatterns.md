# System Patterns: Live Food Agent Architecture

## Core Architecture

### Agent-Based System Design
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Client    │◄──►│  FastAPI Server │◄──►│ Google Gemini   │
│   (Frontend)    │    │   (Backend)     │    │ Live Model      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │              ┌─────────────────┐             │
         └──────────────►│  Tool System    │◄────────────┘
                        │  (Functions)    │
                        └─────────────────┘
```

### Communication Patterns

#### WebSocket Architecture
- **Bidirectional Real-time**: Client ↔ Server instant messaging
- **Session Management**: Individual WebSocket per `session_id`
- **Message Format**: JSON with `mime_type`, `data`, `role` structure
- **Audio Streaming**: Base64-encoded PCM data chunks
- **Error Handling**: Graceful disconnection and reconnection

#### Agent Development Kit (ADK) Integration
```python
# Core agent pattern from app/food/agent.py
root_agent = Agent(
    model="gemini-live-2.5-flash-preview",
    name="ComidaRapidaFantasticaAgent", 
    instruction=top_level_prompt,
    tools=[tool1, tool2, ...]  # Modular tool injection
)
```

## Design Patterns

### 1. Tool-Based Function Architecture
**Pattern**: Each business capability is encapsulated as a discrete tool
**Implementation**: `app/food/tools/tools.py`

```python
# Tool pattern example
def adicionar_item_pedido_tool(session_id: str, producto: str, cantidad: int = 1):
    """Tool for adding items to order"""
    # Validation, state management, business logic
    return standardized_response_format
```

**Benefits**:
- Modular functionality
- Easy testing and maintenance
- Clear separation of concerns
- Reusable across different contexts

### 2. Session-Based State Management
**Pattern**: In-memory dictionary keyed by session_id
**Implementation**: Global `pedidos_en_proceso` dictionary

```python
# State pattern
pedidos_en_proceso = {
    "session_id": {
        "items": [...],
        "total": 0.0
    }
}
```

**Characteristics**:
- **Fast Access**: O(1) lookup by session
- **Temporary Storage**: Development-focused, non-persistent
- **Thread-Safe Operations**: Single-threaded FastAPI context
- **Auto-cleanup**: Manual deletion on order completion

### 3. Event-Driven Audio Processing
**Pattern**: Worklet-based real-time audio handling
**Implementation**: `app/static/js/audio/` directory

```javascript
// Audio worklet pattern
class AudioProcessor extends AudioWorkletProcessor {
    process(inputs, outputs, parameters) {
        // Real-time audio processing
        return true; // Keep alive
    }
}
```

### 4. Three-Column Reactive UI
**Pattern**: Independent, synchronized interface components
**Layout**: Menu | Chat | Order

```html
<!-- UI pattern -->
<div class="container">
    <div class="menu-column">     <!-- Static menu display -->
    <div class="chat-column">     <!-- Real-time conversation -->
    <div class="order-column">    <!-- Live order tracking -->
</div>
```

## Data Flow Patterns

### 1. Order Management Flow
```
User Action → Tool Function → State Update → UI Refresh → Confirmation
```

**Example**: Adding item to order
1. User selects menu item or types request
2. Félix processes with `adicionar_item_pedido_tool`
3. Global state `pedidos_en_proceso` updated
4. Order column refreshes via polling
5. Félix confirms addition verbally

### 2. Real-time Communication Flow
```
Client Message → WebSocket → Agent Processing → Streaming Response → UI Update
```

**Text Flow**:
- Client sends JSON message
- Server routes to appropriate agent session
- Agent processes with tools if needed
- Streaming text response via WebSocket
- Real-time UI updates character by character

**Audio Flow**:
- Client captures PCM audio chunks
- Base64 encoding for WebSocket transmission
- Server processes through Gemini Live
- Response audio streamed back as PCM
- Client audio worklets for playback

### 3. Menu Integration Pattern
```
Static Menu → Click Event → Pre-fill Chat → Natural Processing
```

**Implementation**:
- Menu items have click handlers
- Clicking pre-fills chat input with product name
- Félix processes as natural language request
- Provides context-appropriate responses

## Critical System Components

### 1. Agent Session Management
```python
def start_agent_session(session_id, is_audio=False):
    session = session_service.create_session(...)
    runner = Runner(agent=root_agent, ...)
    live_events = runner.run_live(...)
    return live_events, live_request_queue
```

### 2. Dual-Mode Communication
**Text Mode**: JSON messages with text content
**Audio Mode**: PCM audio streaming with optional transcription

### 3. Tool Orchestration
- **Menu Tools**: `consultar_cardapio_tool`, `calcular_combo_tool`
- **Order Tools**: `adicionar_item_pedido_tool`, `consultar_pedido_atual_tool`
- **Enhancement Tools**: `sugerir_acompanhamentos_tool`
- **Process Tools**: `finalizar_pedido_tool`, `finalize_order_tool`

### 4. Error Handling Patterns
- **Tool Validation**: Input validation in each tool function
- **State Recovery**: Graceful handling of missing session data
- **Communication Resilience**: WebSocket reconnection handling
- **Audio Fallbacks**: Text mode when audio fails

## Scalability Considerations

### Current Limitations
- **In-memory State**: Limited to single server instance
- **No Persistence**: Orders lost on server restart
- **Session Cleanup**: Manual management required

### Future Patterns
- **Database Integration**: Replace in-memory with persistent storage
- **Distributed Sessions**: Redis or similar for multi-server deployment
- **Load Balancing**: WebSocket-aware routing
- **State Synchronization**: Event-driven state updates

This architecture prioritizes real-time responsiveness and development simplicity while maintaining clear separation between AI processing, business logic, and user interface concerns.
