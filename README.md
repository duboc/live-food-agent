# 🍔 Comida Rápida Fantástica - Live Food Agent

Un agente de atención al cliente impulsado por IA para **Comida Rápida Fantástica**, con **Félix, tu Amigo del Sabor** - un asistente virtual entusiasta que ayuda a los clientes a hacer sus pedidos de comida rápida de manera interactiva y divertida.

## 🌟 Características

### 🎯 Agente Conversacional
- **Félix** - Personalidad entusiasta y amigable
- Conversación en **español** con estilo juguetón
- Sugerencias proactivas de combos y upselling
- Manejo inteligente de pedidos complejos

### 🍟 Sistema de Pedidos
- Menú interactivo completo con 4 categorías
- Combos especiales con descuentos automáticos
- Gestión de pedidos en tiempo real
- Cálculo automático de precios y totales

### 🎨 Interfaz de Usuario
- **Layout de 3 columnas**: Menú | Chat | Pedido Actual
- Diseño temático de fast food con colores vibrantes
- Menú clicable que pre-llena el campo de texto
- Actualización en tiempo real del pedido
- Botones de pedido rápido

### 🔊 Capacidades
- **Chat de texto** con respuestas streaming
- **Soporte de voz** bidireccional (español)
- **WebSocket** para comunicación en tiempo real
- **API REST** para gestión de pedidos

## 🚀 Inicio Rápido

### Prerrequisitos
- Python 3.8+
- Clave API de Google Gemini

### Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/duboc/live-food-agent.git
cd live-food-agent
```

2. **Configurar el entorno virtual**
```bash
chmod +x setup_venv.sh
./setup_venv.sh
```

3. **Configurar las variables de entorno**
```bash
cp .env.example .env
# Editar .env y agregar tu GOOGLE_API_KEY
```

4. **Ejecutar la aplicación**
```bash
source venv/bin/activate
cd app
uvicorn main:app --reload
```

5. **Abrir en el navegador**
```
http://localhost:8000
```

## 📁 Estructura del Proyecto

```
live-food-agent/
├── app/
│   ├── main.py              # Servidor FastAPI y WebSocket
│   ├── food/
│   │   ├── agent.py         # Configuración del agente Félix
│   │   └── tools/
│   │       ├── prompts.py   # Personalidad y estrategias de Félix
│   │       └── tools.py     # Herramientas del sistema de pedidos
│   └── static/
│       ├── index.html       # Interfaz web con 3 columnas
│       └── js/
│           ├── app.js       # Lógica del cliente WebSocket
│           └── audio-*.js   # Procesamiento de audio
├── requirements.txt         # Dependencias de Python
└── README.md               # Este archivo
```

## 🍕 Menú Disponible

### 🍔 Sándwiches
- Clásica con Queso CRF - $3.50
- Doble Delicia CRF - $5.00
- Pollo Fantástico Crujiente - $4.00
- Rey Tocino CRF - $6.00
- Y más...

### 🎉 Combos Especiales
- **Combo Fantástico Clásico** - $5.00 (¡Ahorra $2.00!)
- **Combo Doble Delicia** - $7.00 (¡Ahorra $1.50!)
- **Combo Pollo Fantástico** - $6.00
- **Combo Hamburguesita** - $4.00

### 🍟 Acompañamientos
- Papitas Fantásticas (Medianas) - $2.00
- Aros de Cebolla Dorados (M) - $2.50

### 🍨 Postres
- Batido Fantasía (Choc. Croc.) - $3.00
- Conito Helado - $1.00

### 🥤 Bebidas
- Refresco (Mediano) - $1.50
- Jugo de Naranja (Pequeño) - $2.00

## 🛠️ Herramientas del Sistema

El agente Félix utiliza las siguientes herramientas:

1. **consultar_cardapio_tool** - Muestra el menú disponible
2. **calcular_combo_tool** - Calcula precios y descuentos de combos
3. **adicionar_item_pedido_tool** - Agrega items al pedido
4. **consultar_pedido_atual_tool** - Verifica el pedido actual
5. **sugerir_acompanhamentos_tool** - Sugiere complementos
6. **finalizar_pedido_tool** - Procesa el pedido final
7. **limpiar_pedido_tool** - Cancela el pedido actual
8. **calcular_precio_productos_tool** - Calcula precios totales

## 💬 Ejemplos de Uso

### Conversación típica:
```
Usuario: "Hola"
Félix: "¡Qué tal, estrella! ¿Listo/a para algo fantástico? ¡Te recomiendo nuestro Combo Fantástico Clásico!"

Usuario: "Quiero el Combo Doble Delicia"
Félix: "¡Fantástico! El Combo Doble Delicia viene con doble carne, papitas y refresco por solo $7.00"

Usuario: "Agrégame unos aros de cebolla"
Félix: "¡Excelente elección! Los Aros de Cebolla Dorados por $2.50 son espectaculares"

Usuario: "Listo para pagar"
Félix: "¡Perfecto! Tu pedido está confirmado. Total: $9.50"
```

## 🔧 API Endpoints

- `GET /` - Interfaz web principal
- `WebSocket /ws/{session_id}` - Conexión de chat en tiempo real
- `GET /api/pedido/{session_id}` - Obtener pedido actual
- `GET /debug/pedidos` - Ver todos los pedidos en proceso
- `GET /debug/cardapio` - Ver menú completo y combos

## 🎯 Características Técnicas

- **Framework**: FastAPI con WebSocket
- **LLM**: Google Gemini 2.5 Flash Live
- **Audio**: PCM streaming bidireccional
- **Frontend**: HTML5, CSS3, JavaScript vanilla
- **Estado**: In-memory (desarrollo)

## 📝 Notas de Desarrollo

- El sistema usa `session_id = "default"` para desarrollo
- Los pedidos se almacenan en memoria (no persisten)
- El polling del pedido se realiza cada 2 segundos
- Soporte completo para español (es-ES)

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia Apache 2.0 - ver el archivo [LICENSE](LICENSE) para más detalles.

## 🙏 Agradecimientos

- Google ADK por el framework de agentes
- Google Gemini por el modelo de lenguaje
- La comunidad de FastAPI

---

¡Disfruta tu experiencia con **Félix** en **Comida Rápida Fantástica**! 🍔✨
