# 🍗 KFC Live Agent - Asistente KFC para Miércoles de KFC

Un agente de atención al cliente impulsado por IA para **KFC**, con el **Asistente KFC** - un asistente virtual especializado que ayuda a los clientes a hacer sus pedidos de los especiales de Miércoles de KFC de manera interactiva y en español.

## 🌟 Características

### 🎯 Asistente Conversacional KFC
- **Asistente KFC** - Especialista en pollo crujiente y recetas secretas
- Conversación en **español** con enfoque en KFC
- Sugerencias proactivas de combos MDK y upselling
- Manejo inteligente de selección de atributos (receta, complementos, bebidas)

### 🍗 Sistema de Pedidos KFC
- Menú interactivo completo con **Miércoles de KFC**
- **Productos reales**: MDK 6/8/10/12 piezas en solo piezas y combos
- **Atributos complejos**: Recetas (Original/Crispy/Picante), complementos, bebidas
- Precios en **soles peruanos** (S/) con ofertas especiales
- Gestión de pedidos en tiempo real con SKUs

### 🎨 Interfaz de Usuario KFC
- **Branding oficial KFC**: Colores rojo y dorado, diseño temático
- **Layout de 3 columnas**: Menú | Chat | Pedido Actual
- Diseño temático de KFC con elementos visuales atractivos
- Menú clicable que pre-llena el campo de texto
- Actualización en tiempo real del pedido
- Botones de pedido rápido para combos populares

### 🔊 Capacidades Avanzadas
- **Chat de texto** con respuestas streaming
- **Soporte de voz** bidireccional en español (voz "Leda")
- **WebSocket** para comunicación en tiempo real
- **API REST** para gestión de pedidos
- **Flujo conversacional** para selección de atributos

## 🚀 Despliegue en Cloud Run

### Despliegue con Un Solo Comando
```bash
# Hacer el script ejecutable
chmod +x deploy.sh

# Desplegar a Google Cloud Run
./deploy.sh
```

El script automáticamente:
- ✅ Valida tu archivo `.env` con `GOOGLE_API_KEY`
- ✅ Autentica con Google Cloud
- ✅ Configura el proyecto (si es necesario)
- ✅ Habilita las APIs requeridas
- ✅ Despliega con configuraciones optimizadas

### Configuración de Cloud Run
- **Servicio**: `kfc-live-agent`
- **Región**: `us-central1`
- **Memoria**: 2Gi
- **CPU**: 2 cores
- **Acceso**: Público (sin autenticación)
- **Auto-escalado**: 0-10 instancias

📖 **Guía completa**: Ver [DEPLOYMENT.md](DEPLOYMENT.md)

## 🏃‍♂️ Desarrollo Local

### Prerrequisitos
- Python 3.8+
- Clave API de Google Gemini

### Instalación Local

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
# Crear archivo .env con tu API key
echo "GOOGLE_API_KEY=tu_api_key_aqui" > .env
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
│   │   ├── agent.py         # Configuración del Asistente KFC
│   │   └── tools/
│   │       ├── prompts.py   # Personalidad y estrategias KFC
│   │       └── tools.py     # Sistema de menú y pedidos KFC
│   └── static/
│       ├── index.html       # Interfaz KFC con 3 columnas
│       └── js/
│           └── app.js       # Lógica del cliente WebSocket
├── Dockerfile               # Configuración para Cloud Run
├── .gcloudignore           # Exclusiones para despliegue
├── deploy.sh               # Script de despliegue automatizado
├── DEPLOYMENT.md           # Guía de despliegue completa
├── requirements.txt        # Dependencias de Python
└── README.md              # Este archivo
```

## 🍗 Menú KFC Disponible

### 🍗 Solo Piezas (Miércoles de KFC)
- **MDK 6 Piezas** - S/ 19.90
- **MDK 8 Piezas** - S/ 29.90
- **MDK 10 Piezas** - S/ 39.90
- **MDK 12 Piezas** - S/ 49.90

### 🥤 En Combo (Con complemento + bebida)
- **MDK 6 Piezas Combo** - S/ 29.90
- **MDK 8 Piezas Combo** - S/ 39.90
- **MDK 10 Piezas Combo** - S/ 49.90
- **MDK 12 Piezas Combo** - S/ 64.90

### 🎯 Opciones de Personalización
- **Recetas**: Original (11 hierbas y especias), Crispy (extra crujiente), Picante
- **Complementos**: Papa Familiar, Ensalada Familiar, Papa Super Familiar
- **Bebidas**: Coca-Cola Sin Azúcar, Inca Kola Sin Azúcar (1L, 1.5L)

## 🛠️ Herramientas del Sistema

El Asistente KFC utiliza las siguientes herramientas especializadas:

1. **consultar_menu_kfc_tool** - Muestra el menú de KFC disponible
2. **iniciar_seleccion_producto_tool** - Inicia configuración de producto
3. **seleccionar_atributo_tool** - Maneja selección de receta/complemento/bebida
4. **adicionar_producto_finalizado_tool** - Agrega producto configurado al pedido
5. **consultar_pedido_actual_tool** - Verifica el pedido actual
6. **sugerir_complementos_kfc_tool** - Sugiere productos adicionales
7. **finalizar_pedido_kfc_tool** - Procesa el pedido final
8. **limpiar_pedido_tool** - Cancela el pedido actual

## 💬 Ejemplos de Uso

### Flujo típico de conversación:
```
Usuario: "Hola"
Asistente KFC: "¡Bienvenido a KFC! Te recomiendo nuestro MDK 6 Piezas Combo por S/ 29.90"

Usuario: "Quiero MDK 6 piezas combo"
Asistente KFC: "¡Perfecto! ¿Qué receta prefieres: Original, Crispy o Picante?"

Usuario: "Original"
Asistente KFC: "¡Excelente! ¿Qué complemento: Papa Familiar o Ensalada Familiar?"

Usuario: "Papas"
Asistente KFC: "¿Y para beber: Coca-Cola o Inca Kola Sin Azúcar de 1 litro?"

Usuario: "Coca Cola"
Asistente KFC: "¡Listo! He agregado MDK 6 Piezas Combo (Original, Papa Familiar, Coca-Cola Sin Azúcar 1L) por S/ 29.90"
```

## 🔧 API Endpoints

- `GET /` - Interfaz web principal
- `WebSocket /ws/{session_id}` - Conexión de chat en tiempo real
- `GET /api/pedido/{session_id}` - Obtener pedido actual
- `GET /debug/pedidos` - Ver todos los pedidos en proceso
- `GET /debug/menu` - Ver menú completo de KFC

## 🎯 Características Técnicas

- **Framework**: FastAPI con WebSocket
- **LLM**: Google Gemini 2.5 Flash Live
- **Audio**: PCM streaming bidireccional en español
- **Frontend**: HTML5, CSS3, JavaScript vanilla
- **Estado**: In-memory (desarrollo), escalable a base de datos
- **Despliegue**: Google Cloud Run con auto-escalado

## 💰 Costos de Cloud Run

- **Escalado a cero**: $0 cuando no está en uso
- **Pago por uso**: Solo pagas por solicitudes y tiempo de procesamiento
- **Estimado**: Muy bajo para uso moderado (típicamente <$10/mes)

## 🔧 Solución de Problemas

### Desarrollo Local
```bash
# Verificar dependencias
pip install -r requirements.txt

# Verificar variable de entorno
echo $GOOGLE_API_KEY

# Ejecutar con logs
cd app && uvicorn main:app --reload --log-level debug
```

### Cloud Run
```bash
# Ver logs
gcloud run logs tail kfc-live-agent --region us-central1

# Verificar estado del servicio
gcloud run services describe kfc-live-agent --region us-central1
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingKFCFeature`)
3. Commit tus cambios (`git commit -m 'Add some KFC feature'`)
4. Push a la rama (`git push origin feature/AmazingKFCFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia Apache 2.0 - ver el archivo [LICENSE](LICENSE) para más detalles.

---

¡Disfruta tu experiencia con el **Asistente KFC** y los **Miércoles de KFC**! 🍗✨

**¿Listo para desplegar?** Ejecuta `./deploy.sh` y tendrás tu Asistente KFC en la nube en minutos.
