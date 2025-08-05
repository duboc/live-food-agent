import logging
from google.adk.agents import Agent
from food.tools.prompts import top_level_prompt
from food.tools.tools import (
    consultar_menu_kfc_tool,
    iniciar_seleccion_producto_tool,
    seleccionar_atributo_tool,
    adicionar_producto_finalizado_tool,
    consultar_pedido_actual_tool,
    sugerir_complementos_kfc_tool,
    finalizar_pedido_kfc_tool,
    limpiar_pedido_tool,
    calcular_precio_productos_kfc_tool,
    finalize_order_tool
)

logger = logging.getLogger(__name__)

root_agent = Agent(
    model="gemini-live-2.5-flash-preview",
    #model="gemini-2.5-flash-preview-native-audio-dialog",
    name="AsistenteKFC",
    description="Asistente KFC - Especialista en Miércoles de KFC y nuestro famoso pollo crujiente",
    instruction=top_level_prompt,
    tools=[
        consultar_menu_kfc_tool,
        iniciar_seleccion_producto_tool,
        seleccionar_atributo_tool,
        adicionar_producto_finalizado_tool,
        consultar_pedido_actual_tool,
        sugerir_complementos_kfc_tool,
        finalizar_pedido_kfc_tool,
        limpiar_pedido_tool,
        calcular_precio_productos_kfc_tool,
        finalize_order_tool
    ],
)

logger.info(f"Initialized {root_agent.name}")
