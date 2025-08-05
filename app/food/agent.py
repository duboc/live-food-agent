import logging
from google.adk.agents import Agent
from food.tools.prompts import top_level_prompt
from food.tools.tools import (
    consultar_cardapio_tool,
    calcular_combo_tool,
    adicionar_item_pedido_tool,
    consultar_pedido_atual_tool,
    sugerir_acompanhamentos_tool,
    finalizar_pedido_tool,
    limpiar_pedido_tool,
    calcular_precio_productos_tool,
    finalize_order_tool
)

logger = logging.getLogger(__name__)

root_agent = Agent(
    

    # Vertex Model 
    #model="gemini-live-2.5-flash",

    # AI Studio Model
    #model="gemini-live-2.5-flash-preview",

    #Vertex Model 
    model="gemini-live-2.5-flash-preview-native-audio",

    #AI Studio Model
    #model="gemini-2.5-flash-preview-native-audio-dialog",
    name="ComidaRapidaFantasticaAgent",
    description="Félix, el Amigo del Sabor - Agente de atendimento para Comida Rápida Fantástica",
    instruction=top_level_prompt,
    tools=[
        consultar_cardapio_tool,
        calcular_combo_tool,
        adicionar_item_pedido_tool,
        consultar_pedido_atual_tool,
        sugerir_acompanhamentos_tool,
        finalizar_pedido_tool,
        limpiar_pedido_tool,
        calcular_precio_productos_tool,
        finalize_order_tool
    ],
)

logger.info(f"Initialized {root_agent.name}")
