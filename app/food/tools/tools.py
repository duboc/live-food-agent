import logging
from typing import List, Dict, Any, Optional

# Configurar logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# Cardápio da Comida Rápida Fantástica
CARDAPIO_CRF = {
    "SANDWICHES": {
        "Clásica CRF": {
            "descripcion": "Nuestra estrella, sencilla y deliciosa.",
            "ingredientes": "Pan, carne de res, lechuga, tomate, cebolla, pepinillos, salsa especial CRF.",
            "calorias": "550-600",
            "precio": 3.00,
            "destacado": "¡El sabor original de CRF! Sin queso."
        },
        "Clásica con Queso CRF": {
            "descripcion": "La Clásica con una capa de queso derretido.",
            "ingredientes": "Pan, carne de res, queso americano, lechuga, tomate, cebolla, pepinillos, salsa especial CRF.",
            "calorias": "600-650",
            "precio": 3.50,
            "destacado": "Un toque de queso que lo hace irresistible."
        },
        "Doble Delicia CRF": {
            "descripcion": "Doble carne, doble queso, ¡doble sabor!",
            "ingredientes": "Pan, 2 carnes de res, 2 quesos americanos, lechuga, tomate, cebolla, pepinillos, salsa especial CRF.",
            "calorias": "750-850",
            "precio": 5.00,
            "destacado": "Para un hambre voraz."
        },
        "Torre de Sabor CRF": {
            "descripcion": "Dos carnes, queso y nuestra salsa Torre secreta.",
            "ingredientes": "Pan, 2 carnes de res, queso cheddar, tocino crujiente, salsa Torre.",
            "calorias": "800-900",
            "precio": 5.50,
            "destacado": "¡Una explosión de sabor!"
        },
        "Rey Tocino CRF": {
            "descripcion": "Mucha carne, queso y tocino para los reyes.",
            "ingredientes": "Pan, 2 carnes de res, queso cheddar, abundante tocino, kétchup, mayonesa.",
            "calorias": "900-1000",
            "precio": 6.00,
            "destacado": "El paraíso para los amantes del tocino."
        },
        "Gran Rey CRF": {
            "descripcion": "Dos carnes jugosas con nuestra salsa Rey.",
            "ingredientes": "Pan triple, 2 carnes de res, queso americano, lechuga, cebolla, pepinillos, salsa Rey.",
            "calorias": "500-550",
            "precio": 4.50,
            "destacado": "Un clásico reinventado."
        },
        "Pollo Fantástico Crujiente": {
            "descripcion": "Filete de pollo empanizado y extra crujiente.",
            "ingredientes": "Pan, filete de pollo crujiente, lechuga, tomate, mayonesa.",
            "calorias": "450-500",
            "precio": 4.00,
            "destacado": "¡Super crujiente y delicioso!"
        },
        "Hamburguesa Vegetal Fantástica": {
            "descripcion": "Sabor increíble, ¡100% a base de plantas!",
            "ingredientes": "Pan, medallón vegetal, lechuga, tomate, cebolla, pepinillos, mayonesa (opcional vegana).",
            "calorias": "500-550",
            "precio": 5.00,
            "destacado": "¡Para todos los gustos!"
        },
        "Hamburguesita con Queso": {
            "descripcion": "Simple, clásica y deliciosa.",
            "ingredientes": "Pan, carne de res, queso americano, pepinillos, kétchup, mostaza.",
            "calorias": "300-350",
            "precio": 1.50,
            "destacado": "Perfecta para un antojo o para niños."
        },
        "Doble Queso Económica": {
            "descripcion": "Dos carnes y queso, ¡directo al punto!",
            "ingredientes": "Pan, 2 carnes de res, 2 quesos americanos, pepinillos, kétchup, mostaza.",
            "calorias": "400-450",
            "precio": 2.50,
            "destacado": "¡Doble sabor a un precio increíble!"
        }
    },
    "ACOMPAÑAMIENTOS": {
        "Papitas Fantásticas (Medianas)": {
            "descripcion": "Doradas y crujientes, ¡el acompañante perfecto!",
            "ingredientes": "Papas, aceite vegetal, sal.",
            "calorias": "300-350",
            "precio": 2.00,
            "destacado": "¡Irresistibles!"
        },
        "Aros de Cebolla Dorados (M)": {
            "descripcion": "Crujientes por fuera, tiernos por dentro.",
            "ingredientes": "Cebolla, empanizado especial, aceite vegetal, sal.",
            "calorias": "320-380",
            "precio": 2.50,
            "destacado": "Un clásico con nuestro toque."
        },
        "Bocaditos de Pollo Mágicos (6u)": {
            "descripcion": "Tiernos trocitos de pollo empanizado.",
            "ingredientes": "Carne de pollo, empanizado, aceite vegetal, especias.",
            "calorias": "220-280",
            "precio": 2.50,
            "destacado": "¡Ideales para dipear!"
        },
        "Papas Mágicas (para compartir)": {
            "descripcion": "¡Una montaña de papas para todos!",
            "ingredientes": "Papas, aceite vegetal, sal.",
            "calorias": "700-800",
            "precio": 4.00,
            "destacado": "¡Perfectas para el grupo!"
        }
    },
    "POSTRES": {
        "Batido Fantasía (Choc. Croc.)": {
            "descripcion": "Cremoso batido con trocitos crocantes de chocolate.",
            "ingredientes": "Helado de vainilla, leche, sirope de chocolate, trocitos crocantes de galleta.",
            "calorias": "450-550",
            "precio": 3.00,
            "destacado": "¡Una explosión de texturas!"
        },
        "Batido Clásico de Chocolate": {
            "descripcion": "El sabor clásico del chocolate en un batido.",
            "ingredientes": "Helado de vainilla, leche, sirope de chocolate intenso.",
            "calorias": "400-500",
            "precio": 2.50,
            "destacado": "Simple y delicioso."
        },
        "Copa Helada Clásica (Choc/Fresa)": {
            "descripcion": "Helado de vainilla con tu sirope favorito.",
            "ingredientes": "Helado de vainilla, sirope (chocolate o fresa).",
            "calorias": "200-250",
            "precio": 1.50,
            "destacado": "Un final dulce y refrescante."
        },
        "Conito Helado": {
            "descripcion": "Vainilla, chocolate o mixto. ¡Un clásico!",
            "ingredientes": "Masa de helado.",
            "calorias": "120-150",
            "precio": 1.00,
            "destacado": "¡La opción más económica y refrescante!"
        },
        "Mezcla Mágica (Trocitos Croc.)": {
            "descripcion": "Helado mezclado con toppings deliciosos.",
            "ingredientes": "Helado de vainilla, trocitos crocantes de galleta/chocolate.",
            "calorias": "300-400",
            "precio": 2.50,
            "destacado": "¡Crea tu propia magia!"
        }
    },
    "BEBIDAS": {
        "Refresco (Mediano)": {
            "descripcion": "Varios sabores disponibles.",
            "ingredientes": "Varía según el sabor.",
            "calorias": "150-180 (con azúcar)",
            "precio": 1.50,
            "destacado": "Opciones con o sin azúcar."
        },
        "Agua Embotellada": {
            "descripcion": "Natural o con gas.",
            "ingredientes": "Agua mineral.",
            "calorias": "0",
            "precio": 1.00,
            "destacado": "La opción más saludable."
        },
        "Jugo de Naranja (Pequeño)": {
            "descripcion": "Natural y refrescante.",
            "ingredientes": "Naranja.",
            "calorias": "100-120",
            "precio": 2.00,
            "destacado": "¡Pura vitamina C!"
        }
    }
}

# Combos predefinidos con descuentos
COMBOS_CRF = {
    "Combo Fantástico Clásico": {
        "componentes": ["Clásica con Queso CRF", "Papitas Fantásticas (Medianas)", "Refresco (Mediano)"],
        "precio_individual": 7.00,
        "precio_combo": 5.00,
        "ahorro": 2.00
    },
    "Combo Doble Delicia": {
        "componentes": ["Doble Delicia CRF", "Papitas Fantásticas (Medianas)", "Refresco (Mediano)"],
        "precio_individual": 8.50,
        "precio_combo": 7.00,
        "ahorro": 1.50
    },
    "Combo Pollo Fantástico": {
        "componentes": ["Pollo Fantástico Crujiente", "Papitas Fantásticas (Medianas)", "Refresco (Mediano)"],
        "precio_individual": 7.50,
        "precio_combo": 6.00,
        "ahorro": 1.50
    },
    "Combo Hamburguesita": {
        "componentes": ["Hamburguesita con Queso", "Papitas Fantásticas (Medianas)", "Refresco (Mediano)"],
        "precio_individual": 5.00,
        "precio_combo": 4.00,
        "ahorro": 1.00
    }
}

# Variable global para almacenar pedidos en construcción
pedidos_en_proceso = {}


def consultar_cardapio_tool(categoria: Optional[str] = None) -> Dict[str, Any]:
    """
    Consultar el cardápio completo o por categoría específica.

    Args:
        categoria: Categoría específica (SANDWICHES, ACOMPAÑAMIENTOS, POSTRES, BEBIDAS)

    Returns:
        Información del cardápio
    """
    logger.info(f"Consultando cardápio - categoría: {categoria}")
    
    if categoria and categoria.upper() in CARDAPIO_CRF:
        return {
            "categoria": categoria.upper(),
            "productos": CARDAPIO_CRF[categoria.upper()]
        }
    
    return {
        "cardapio_completo": CARDAPIO_CRF,
        "combos_disponibles": COMBOS_CRF
    }


def calcular_combo_tool(nombre_combo: str) -> Dict[str, Any]:
    """
    Calcular precio y componentes de un combo específico.

    Args:
        nombre_combo: Nombre del combo a calcular

    Returns:
        Detalles del combo con precio y ahorro
    """
    logger.info(f"Calculando combo: {nombre_combo}")
    
    if nombre_combo not in COMBOS_CRF:
        return {"error": f"Combo '{nombre_combo}' no encontrado"}
    
    combo = COMBOS_CRF[nombre_combo]
    
    return {
        "nombre": nombre_combo,
        "componentes": combo["componentes"],
        "precio_individual": combo["precio_individual"],
        "precio_combo": combo["precio_combo"],
        "ahorro": combo["ahorro"],
        "descripcion": f"Ahorra ${combo['ahorro']:.2f} con este combo fantástico!"
    }


def adicionar_item_pedido_tool(session_id: str, producto: str, cantidad: int = 1) -> Dict[str, Any]:
    """
    Adicionar un item al pedido en construcción.

    Args:
        session_id: ID de la sesión del cliente
        producto: Nombre del producto a agregar
        cantidad: Cantidad del producto

    Returns:
        Estado actual del pedido
    """
    logger.info(f"Adicionando item - Session: {session_id}, Producto: {producto}, Cantidad: {cantidad}")
    
    # Buscar el producto en el cardápio
    producto_encontrado = None
    precio_unitario = 0
    
    for categoria, productos in CARDAPIO_CRF.items():
        if producto in productos:
            producto_encontrado = productos[producto]
            precio_unitario = producto_encontrado["precio"]
            break
    
    if not producto_encontrado:
        return {"error": f"Producto '{producto}' no encontrado en el cardápio"}
    
    # Inicializar pedido si no existe
    if session_id not in pedidos_en_proceso:
        pedidos_en_proceso[session_id] = {
            "items": [],
            "total": 0.0
        }
    
    # Verificar si el producto ya está en el pedido
    item_existente = None
    for item in pedidos_en_proceso[session_id]["items"]:
        if item["producto"] == producto:
            item_existente = item
            break
    
    if item_existente:
        item_existente["cantidad"] += cantidad
        item_existente["subtotal"] = item_existente["cantidad"] * precio_unitario
    else:
        nuevo_item = {
            "producto": producto,
            "cantidad": cantidad,
            "precio_unitario": precio_unitario,
            "subtotal": cantidad * precio_unitario
        }
        pedidos_en_proceso[session_id]["items"].append(nuevo_item)
    
    # Recalcular total
    pedidos_en_proceso[session_id]["total"] = sum(
        item["subtotal"] for item in pedidos_en_proceso[session_id]["items"]
    )
    
    return {
        "item_agregado": {
            "producto": producto,
            "cantidad": cantidad,
            "precio_unitario": precio_unitario
        },
        "pedido_actual": pedidos_en_proceso[session_id]
    }


def consultar_pedido_atual_tool(session_id: str) -> Dict[str, Any]:
    """
    Consultar el estado actual del pedido en construcción.

    Args:
        session_id: ID de la sesión del cliente

    Returns:
        Estado actual del pedido
    """
    logger.info(f"Consultando pedido atual - Session: {session_id}")
    
    if session_id not in pedidos_en_proceso:
        return {
            "pedido_vacio": True,
            "mensaje": "No hay items en el pedido actual"
        }
    
    return {
        "pedido_vacio": False,
        "pedido": pedidos_en_proceso[session_id]
    }


def sugerir_acompanhamentos_tool(productos_actuales: List[str]) -> Dict[str, Any]:
    """
    Sugerir acompañamientos basados en los productos actuales del pedido.

    Args:
        productos_actuales: Lista de productos ya en el pedido

    Returns:
        Sugerencias de acompañamientos y postres
    """
    logger.info(f"Generando sugerencias para productos: {productos_actuales}")
    
    tiene_sandwich = any(prod in CARDAPIO_CRF["SANDWICHES"] for prod in productos_actuales)
    tiene_acompanamiento = any(prod in CARDAPIO_CRF["ACOMPAÑAMIENTOS"] for prod in productos_actuales)
    tiene_bebida = any(prod in CARDAPIO_CRF["BEBIDAS"] for prod in productos_actuales)
    tiene_postre = any(prod in CARDAPIO_CRF["POSTRES"] for prod in productos_actuales)
    
    sugerencias = []
    
    if tiene_sandwich and not tiene_acompanamiento:
        sugerencias.extend([
            "Aros de Cebolla Dorados (M) - ¡Solo $2.50 y son espectaculares!",
            "Papitas Fantásticas (Medianas) - ¡El acompañante perfecto por $2.00!"
        ])
    
    if not tiene_bebida:
        sugerencias.append("Refresco (Mediano) - ¡Completa tu comida por solo $1.50!")
    
    if not tiene_postre:
        sugerencias.extend([
            "Batido Fantasía (Choc. Croc.) - ¡Una explosión de texturas por $3.00!",
            "Conito Helado - ¡La opción más económica y refrescante por $1.00!"
        ])
    
    if len(productos_actuales) > 1:
        sugerencias.append("Papas Mágicas (para compartir) - ¡Ideales para el grupo por $4.00!")
    
    return {
        "tiene_sandwich": tiene_sandwich,
        "sugerencias": sugerencias,
        "mensaje": "¿Te animas a probar alguno de estos para completar tu experiencia fantástica?"
    }


def finalizar_pedido_tool(session_id: str) -> Dict[str, Any]:
    """
    Finalizar el pedido y preparar los datos para la función finalizeOrder.

    Args:
        session_id: ID de la sesión del cliente

    Returns:
        Datos del pedido para finalizeOrder
    """
    logger.info(f"Finalizando pedido - Session: {session_id}")
    
    if session_id not in pedidos_en_proceso:
        return {
            "error": "No hay pedido para finalizar",
            "mensaje": "Primero necesitas agregar productos a tu pedido"
        }
    
    pedido = pedidos_en_proceso[session_id]
    
    if not pedido["items"]:
        return {
            "error": "Pedido vacío",
            "mensaje": "No hay items en el pedido para finalizar"
        }
    
    # Preparar orderItems para la función finalizeOrder
    order_items = []
    for item in pedido["items"]:
        order_items.append({
            "productName": item["producto"],
            "quantity": item["cantidad"]
        })
    
    # Limpiar el pedido después de finalizar
    del pedidos_en_proceso[session_id]
    
    return {
        "success": True,
        "orderItems": order_items,
        "total": pedido["total"],
        "resumen_pedido": pedido,
        "mensaje": "Pedido listo para finalizeOrder"
    }


def limpiar_pedido_tool(session_id: str) -> Dict[str, Any]:
    """
    Limpiar/cancelar el pedido actual.

    Args:
        session_id: ID de la sesión del cliente

    Returns:
        Confirmación de limpieza
    """
    logger.info(f"Limpiando pedido - Session: {session_id}")
    
    if session_id in pedidos_en_proceso:
        del pedidos_en_proceso[session_id]
        return {"success": True, "mensaje": "Pedido cancelado exitosamente"}
    
    return {"success": True, "mensaje": "No había pedido para cancelar"}


def calcular_precio_productos_tool(productos: List[str]) -> Dict[str, Any]:
    """
    Calcular el precio total de una lista de productos.

    Args:
        productos: Lista de nombres de productos

    Returns:
        Cálculo de precios individuales y total
    """
    logger.info(f"Calculando precios para productos: {productos}")
    
    resultados = []
    total = 0.0
    
    for producto in productos:
        precio = None
        categoria_encontrada = None
        
        for categoria, items in CARDAPIO_CRF.items():
            if producto in items:
                precio = items[producto]["precio"]
                categoria_encontrada = categoria
                break
        
        if precio is not None:
            resultados.append({
                "producto": producto,
                "categoria": categoria_encontrada,
                "precio": precio
            })
            total += precio
        else:
            resultados.append({
                "producto": producto,
                "error": "Producto no encontrado"
            })
    
    return {
        "productos": resultados,
        "total": total
    }


def finalize_order_tool(order_items: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Simular la función finalizeOrder para procesar el pedido final.
    Esta función simula el envío del pedido a un sistema externo.

    Args:
        order_items: Lista de items del pedido con formato [{"productName": str, "quantity": int}]

    Returns:
        Resultado del procesamiento del pedido
    """
    import random
    import time
    
    logger.info(f"Procesando pedido final con items: {order_items}")
    
    # Validar formato de order_items
    if not isinstance(order_items, list):
        return {
            "status": "ERROR",
            "error": "order_items debe ser una lista",
            "message": "Formato de pedido inválido"
        }
    
    for item in order_items:
        if not isinstance(item, dict) or "productName" not in item or "quantity" not in item:
            return {
                "status": "ERROR",
                "error": "Cada item debe tener productName y quantity",
                "message": "Formato de item inválido"
            }
    
    # Simular tiempo de procesamiento
    time.sleep(0.5)
    
    # Simular éxito en 95% de los casos
    if random.random() < 0.95:
        order_id = f"CRF-{random.randint(100000, 999999)}"
        total_items = sum(item["quantity"] for item in order_items)
        
        logger.info(f"Pedido procesado exitosamente - ID: {order_id}")
        
        return {
            "status": "SUCCESS",
            "orderId": order_id,
            "message": "Pedido procesado exitosamente",
            "items": order_items,
            "totalItems": total_items,
            "estimatedTime": "15-20 minutos"
        }
    else:
        logger.warning("Simulando error en procesamiento de pedido")
        
        return {
            "status": "ERROR",
            "error": "Error en el sistema de pedidos",
            "message": "Por favor intenta nuevamente en unos momentos"
        }
