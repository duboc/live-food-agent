import logging
from typing import List, Dict, Any, Optional

# Configurar logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# Menú de KFC - Miércoles de KFC
KFC_MENU = {
    "SOLO_PIEZAS": {
        "MDK 6 PIEZAS": {
            "nombre_completo": "Miércoles de KFC: 6 Piezas",
            "descripcion": "6 deliciosas piezas de pollo con la receta que prefieras",
            "precio": 19.90,
            "sku": "13638",
            "atributos_requeridos": {
                "receta": {
                    "nombre": "Elige la Receta",
                    "opciones": {
                        "Receta Original": {"id": "79", "descripcion": "El sabor clásico de KFC"},
                        "Crispy": {"id": "80", "descripcion": "Extra crujiente y dorado"},
                        "Picante": {"id": "11233", "descripcion": "Con especias picantes"}
                    }
                }
            },
            "categoria": "solo_piezas"
        },
        "MDK 8 PIEZAS": {
            "nombre_completo": "Miércoles de KFC: 8 Piezas",
            "descripcion": "8 jugosas piezas de pollo para compartir",
            "precio": 29.90,
            "sku": "12554",
            "atributos_requeridos": {
                "receta": {
                    "nombre": "Elige la Receta",
                    "opciones": {
                        "Receta Original": {"id": "79", "descripcion": "El sabor clásico de KFC"},
                        "Crispy": {"id": "80", "descripcion": "Extra crujiente y dorado"},
                        "Picante": {"id": "11233", "descripcion": "Con especias picantes"}
                    }
                }
            },
            "categoria": "solo_piezas"
        },
        "MDK 10 PIEZAS": {
            "nombre_completo": "Miércoles de KFC: 10 Piezas",
            "descripcion": "10 piezas irresistibles para toda la familia",
            "precio": 39.90,
            "sku": "11492",
            "atributos_requeridos": {
                "receta": {
                    "nombre": "Elige la Receta",
                    "opciones": {
                        "Receta Original": {"id": "79", "descripcion": "El sabor clásico de KFC"},
                        "Crispy": {"id": "80", "descripcion": "Extra crujiente y dorado"},
                        "Picante": {"id": "11233", "descripcion": "Con especias picantes"}
                    }
                }
            },
            "categoria": "solo_piezas"
        },
        "MDK 12 PIEZAS": {
            "nombre_completo": "Miércoles de KFC: 12 Piezas",
            "descripcion": "12 piezas perfectas para grupos grandes",
            "precio": 49.90,
            "sku": "15650",
            "atributos_requeridos": {
                "receta": {
                    "nombre": "Elige la Receta",
                    "opciones": {
                        "Receta Original": {"id": "79", "descripcion": "El sabor clásico de KFC"},
                        "Crispy": {"id": "80", "descripcion": "Extra crujiente y dorado"},
                        "Picante": {"id": "11233", "descripcion": "Con especias picantes"}
                    }
                }
            },
            "categoria": "solo_piezas"
        }
    },
    "EN_COMBO": {
        "MDK 6 PIEZAS COMBO": {
            "nombre_completo": "Miércoles de KFC: 6 Piezas en Combo",
            "descripcion": "6 piezas + complemento + bebida familiar",
            "precio": 29.90,
            "sku": "13639",
            "atributos_requeridos": {
                "receta": {
                    "nombre": "Elige la Receta",
                    "opciones": {
                        "Receta Original": {"id": "79", "descripcion": "El sabor clásico de KFC"},
                        "Crispy": {"id": "80", "descripcion": "Extra crujiente y dorado"},
                        "Picante": {"id": "11233", "descripcion": "Con especias picantes"}
                    }
                },
                "complemento": {
                    "nombre": "Elige tu complemento",
                    "opciones": {
                        "Papa Familiar": {"id": "102", "descripcion": "Papas fritas familiares para compartir"},
                        "Ensalada Familiar": {"id": "113", "descripcion": "Ensalada fresca familiar"}
                    }
                },
                "bebida": {
                    "nombre": "Elige el sabor de tu bebida",
                    "opciones": {
                        "Coca-Cola Sin Azúcar 1L": {"id": "12194", "descripcion": "Coca-Cola sin azúcar 1 litro"},
                        "Inca Kola Sin Azúcar 1L": {"id": "12196", "descripcion": "Inca Kola sin azúcar 1 litro"}
                    }
                }
            },
            "categoria": "combo"
        },
        "MDK 8 PIEZAS COMBO": {
            "nombre_completo": "Miércoles de KFC: 8 Piezas en Combo",
            "descripcion": "8 piezas + complemento + bebida familiar",
            "precio": 39.90,
            "sku": "16284",
            "atributos_requeridos": {
                "receta": {
                    "nombre": "Elige la Receta",
                    "opciones": {
                        "Receta Original": {"id": "79", "descripcion": "El sabor clásico de KFC"},
                        "Crispy": {"id": "80", "descripcion": "Extra crujiente y dorado"},
                        "Picante": {"id": "11233", "descripcion": "Con especias picantes"}
                    }
                },
                "complemento": {
                    "nombre": "Elige tu complemento",
                    "opciones": {
                        "Papa Familiar": {"id": "102", "descripcion": "Papas fritas familiares para compartir"},
                        "Ensalada Familiar": {"id": "113", "descripcion": "Ensalada fresca familiar"}
                    }
                },
                "bebida": {
                    "nombre": "Elige el sabor de tu bebida",
                    "opciones": {
                        "Coca-Cola Sin Azúcar 1L": {"id": "12194", "descripcion": "Coca-Cola sin azúcar 1 litro"},
                        "Inca Kola Sin Azúcar 1L": {"id": "12196", "descripcion": "Inca Kola sin azúcar 1 litro"}
                    }
                }
            },
            "categoria": "combo"
        },
        "MDK 10 PIEZAS COMBO": {
            "nombre_completo": "Miércoles de KFC: 10 Piezas en Combo",
            "descripcion": "10 piezas + complemento + bebida grande",
            "precio": 49.90,
            "sku": "13640",
            "atributos_requeridos": {
                "receta": {
                    "nombre": "Elige la Receta",
                    "opciones": {
                        "Receta Original": {"id": "79", "descripcion": "El sabor clásico de KFC"},
                        "Crispy": {"id": "80", "descripcion": "Extra crujiente y dorado"},
                        "Picante": {"id": "11233", "descripcion": "Con especias picantes"}
                    }
                },
                "complemento": {
                    "nombre": "Elige tu complemento",
                    "opciones": {
                        "Papa Familiar": {"id": "102", "descripcion": "Papas fritas familiares para compartir"},
                        "Ensalada Familiar": {"id": "113", "descripcion": "Ensalada fresca familiar"}
                    }
                },
                "bebida": {
                    "nombre": "Elige el sabor de tu bebida",
                    "opciones": {
                        "Inca Kola Sin Azúcar 1.5L": {"id": "110", "descripcion": "Inca Kola sin azúcar 1.5 litros"},
                        "Coca-Cola Sin Azúcar 1.5L": {"id": "111", "descripcion": "Coca-Cola sin azúcar 1.5 litros"}
                    }
                }
            },
            "categoria": "combo"
        },
        "MDK 12 PIEZAS COMBO": {
            "nombre_completo": "Miércoles de KFC: 12 Piezas en Combo",
            "descripcion": "12 piezas + complemento súper familiar + bebida grande",
            "precio": 64.90,
            "sku": "15990",
            "atributos_requeridos": {
                "receta": {
                    "nombre": "Elige la Receta",
                    "opciones": {
                        "Receta Original": {"id": "79", "descripcion": "El sabor clásico de KFC"},
                        "Crispy": {"id": "80", "descripcion": "Extra crujiente y dorado"},
                        "Picante": {"id": "11233", "descripcion": "Con especias picantes"}
                    }
                },
                "complemento": {
                    "nombre": "Elige tu complemento",
                    "opciones": {
                        "Papa Super Familiar": {"id": "15098", "descripcion": "Papas súper familiares para toda la familia"}
                    }
                },
                "bebida": {
                    "nombre": "Elige el sabor de tu bebida",
                    "opciones": {
                        "Inca Kola Sin Azúcar 1.5L": {"id": "110", "descripcion": "Inca Kola sin azúcar 1.5 litros"},
                        "Coca-Cola Sin Azúcar 1.5L": {"id": "111", "descripcion": "Coca-Cola sin azúcar 1.5 litros"}
                    }
                }
            },
            "categoria": "combo"
        }
    }
}

# Variable global para almacenar pedidos en construcción y selecciones pendientes
pedidos_en_proceso = {}
selecciones_pendientes = {}


def consultar_menu_kfc_tool(categoria: Optional[str] = None) -> Dict[str, Any]:
    """
    Consultar el menú completo de KFC o por categoría específica.

    Args:
        categoria: Categoría específica (SOLO_PIEZAS, EN_COMBO)

    Returns:
        Información del menú KFC
    """
    logger.info(f"Consultando menú KFC - categoría: {categoria}")
    
    if categoria and categoria.upper() in KFC_MENU:
        return {
            "categoria": categoria.upper(),
            "productos": KFC_MENU[categoria.upper()],
            "mensaje": f"Aquí tienes los productos de {categoria.replace('_', ' ').title()}"
        }
    
    return {
        "menu_completo": KFC_MENU,
        "categorias": ["SOLO_PIEZAS", "EN_COMBO"],
        "mensaje": "¡Bienvenido a KFC! Estos son nuestros especiales de Miércoles de KFC"
    }


def iniciar_seleccion_producto_tool(session_id: str, nombre_producto: str) -> Dict[str, Any]:
    """
    Iniciar el proceso de selección de un producto KFC con sus atributos.

    Args:
        session_id: ID de la sesión del cliente
        nombre_producto: Nombre del producto KFC a configurar

    Returns:
        Primera pregunta sobre atributos o confirmación si no requiere atributos
    """
    logger.info(f"Iniciando selección de producto - Session: {session_id}, Producto: {nombre_producto}")
    
    # Buscar el producto en el menú
    producto_encontrado = None
    categoria_producto = None
    
    for categoria, productos in KFC_MENU.items():
        if nombre_producto in productos:
            producto_encontrado = productos[nombre_producto]
            categoria_producto = categoria
            break
    
    if not producto_encontrado:
        return {"error": f"Producto '{nombre_producto}' no encontrado en el menú KFC"}
    
    # Inicializar selección pendiente
    if session_id not in selecciones_pendientes:
        selecciones_pendientes[session_id] = {}
    
    selecciones_pendientes[session_id] = {
        "producto": nombre_producto,
        "categoria": categoria_producto,
        "atributos_seleccionados": {},
        "atributos_pendientes": list(producto_encontrado.get("atributos_requeridos", {}).keys()),
        "precio": producto_encontrado["precio"],
        "sku": producto_encontrado["sku"]
    }
    
    # Si no requiere atributos, agregar directamente
    if not producto_encontrado.get("atributos_requeridos"):
        return adicionar_producto_finalizado_tool(session_id)
    
    # Obtener primer atributo pendiente
    primer_atributo = selecciones_pendientes[session_id]["atributos_pendientes"][0]
    atributo_info = producto_encontrado["atributos_requeridos"][primer_atributo]
    
    opciones_texto = []
    for opcion, datos in atributo_info["opciones"].items():
        opciones_texto.append(f"• {opcion}: {datos['descripcion']}")
    
    return {
        "producto": nombre_producto,
        "categoria": categoria_producto,
        "precio": producto_encontrado["precio"],
        "atributo_actual": primer_atributo,
        "pregunta": atributo_info["nombre"],
        "opciones": list(atributo_info["opciones"].keys()),
        "opciones_detalle": opciones_texto,
        "mensaje": f"¡Perfecto! Has elegido {nombre_producto} por S/ {producto_encontrado['precio']:.2f}. Ahora necesito que elijas: {atributo_info['nombre']}"
    }


def seleccionar_atributo_tool(session_id: str, atributo: str, valor: str) -> Dict[str, Any]:
    """
    Seleccionar un valor para un atributo del producto en configuración.

    Args:
        session_id: ID de la sesión del cliente
        atributo: Nombre del atributo (receta, complemento, bebida)
        valor: Valor seleccionado para el atributo

    Returns:
        Siguiente pregunta de atributo o confirmación final
    """
    logger.info(f"Seleccionando atributo - Session: {session_id}, Atributo: {atributo}, Valor: {valor}")
    
    if session_id not in selecciones_pendientes:
        return {"error": "No hay producto en selección. Primero elige un producto."}
    
    seleccion = selecciones_pendientes[session_id]
    producto_info = KFC_MENU[seleccion["categoria"]][seleccion["producto"]]
    
    # Validar que el atributo existe y el valor es válido
    if atributo not in producto_info.get("atributos_requeridos", {}):
        return {"error": f"Atributo '{atributo}' no válido para este producto"}
    
    opciones_validas = producto_info["atributos_requeridos"][atributo]["opciones"]
    if valor not in opciones_validas:
        return {"error": f"Opción '{valor}' no válida para {atributo}"}
    
    # Guardar selección
    seleccion["atributos_seleccionados"][atributo] = valor
    
    # Remover de pendientes
    if atributo in seleccion["atributos_pendientes"]:
        seleccion["atributos_pendientes"].remove(atributo)
    
    # Si quedan atributos pendientes, preguntar el siguiente
    if seleccion["atributos_pendientes"]:
        siguiente_atributo = seleccion["atributos_pendientes"][0]
        atributo_info = producto_info["atributos_requeridos"][siguiente_atributo]
        
        opciones_texto = []
        for opcion, datos in atributo_info["opciones"].items():
            opciones_texto.append(f"• {opcion}: {datos['descripcion']}")
        
        return {
            "atributo_guardado": f"{atributo}: {valor}",
            "atributo_actual": siguiente_atributo,
            "pregunta": atributo_info["nombre"],
            "opciones": list(atributo_info["opciones"].keys()),
            "opciones_detalle": opciones_texto,
            "mensaje": f"¡Excelente! Has elegido {valor}. Ahora: {atributo_info['nombre']}"
        }
    
    # Todos los atributos completados, agregar al pedido
    return adicionar_producto_finalizado_tool(session_id)


def adicionar_producto_finalizado_tool(session_id: str) -> Dict[str, Any]:
    """
    Agregar el producto completamente configurado al pedido.

    Args:
        session_id: ID de la sesión del cliente

    Returns:
        Confirmación del producto agregado al pedido
    """
    logger.info(f"Finalizando adición de producto - Session: {session_id}")
    
    if session_id not in selecciones_pendientes:
        return {"error": "No hay producto configurado para agregar"}
    
    seleccion = selecciones_pendientes[session_id]
    
    # Inicializar pedido si no existe
    if session_id not in pedidos_en_proceso:
        pedidos_en_proceso[session_id] = {
            "items": [],
            "total": 0.0
        }
    
    # Crear nombre completo del producto con atributos
    nombre_completo = seleccion["producto"]
    if seleccion["atributos_seleccionados"]:
        detalles = []
        for atributo, valor in seleccion["atributos_seleccionados"].items():
            detalles.append(f"{valor}")
        nombre_completo += f" ({', '.join(detalles)})"
    
    # Agregar al pedido
    nuevo_item = {
        "producto": nombre_completo,
        "producto_base": seleccion["producto"],
        "atributos": seleccion["atributos_seleccionados"],
        "cantidad": 1,
        "precio_unitario": seleccion["precio"],
        "subtotal": seleccion["precio"],
        "sku": seleccion["sku"],
        "categoria": seleccion["categoria"]
    }
    
    pedidos_en_proceso[session_id]["items"].append(nuevo_item)
    
    # Recalcular total
    pedidos_en_proceso[session_id]["total"] = sum(
        item["subtotal"] for item in pedidos_en_proceso[session_id]["items"]
    )
    
    # Limpiar selección pendiente
    del selecciones_pendientes[session_id]
    
    return {
        "item_agregado": nuevo_item,
        "pedido_actual": pedidos_en_proceso[session_id],
        "mensaje": f"¡Perfecto! He agregado {nombre_completo} por S/ {seleccion['precio']:.2f} a tu pedido."
    }


def consultar_pedido_actual_tool(session_id: str) -> Dict[str, Any]:
    """
    Consultar el estado actual del pedido en construcción.

    Args:
        session_id: ID de la sesión del cliente

    Returns:
        Estado actual del pedido
    """
    logger.info(f"Consultando pedido actual - Session: {session_id}")
    
    if session_id not in pedidos_en_proceso:
        return {
            "pedido_vacio": True,
            "mensaje": "No tienes productos en tu pedido actual"
        }
    
    pedido = pedidos_en_proceso[session_id]
    
    # Formatear resumen del pedido
    resumen_items = []
    for item in pedido["items"]:
        resumen_items.append(f"• {item['producto']} - S/ {item['subtotal']:.2f}")
    
    return {
        "pedido_vacio": False,
        "pedido": pedido,
        "resumen": resumen_items,
        "total_formateado": f"S/ {pedido['total']:.2f}",
        "cantidad_items": len(pedido["items"]),
        "mensaje": f"Tu pedido actual tiene {len(pedido['items'])} productos por un total de S/ {pedido['total']:.2f}"
    }


def sugerir_complementos_kfc_tool(productos_actuales: List[str]) -> Dict[str, Any]:
    """
    Sugerir productos adicionales basados en el pedido actual.

    Args:
        productos_actuales: Lista de productos ya en el pedido

    Returns:
        Sugerencias de productos adicionales
    """
    logger.info(f"Generando sugerencias KFC para productos: {productos_actuales}")
    
    tiene_solo_piezas = any("MDK" in prod and "COMBO" not in prod for prod in productos_actuales)
    tiene_combo = any("COMBO" in prod for prod in productos_actuales)
    
    sugerencias = []
    
    if tiene_solo_piezas:
        sugerencias.extend([
            "¿Te gustaría convertir tu pedido en combo? ¡Incluye complemento y bebida por solo S/ 10.00 más!",
            "¿Qué tal si agregamos más piezas? Tenemos ofertas especiales en MDK 8, 10 o 12 piezas."
        ])
    
    if not tiene_combo and not tiene_solo_piezas:
        sugerencias.extend([
            "Te recomiendo nuestro MDK 6 Piezas Combo por S/ 29.90 - ¡6 piezas + complemento + bebida!",
            "¿Prefieres solo las piezas? MDK 6 Piezas por S/ 19.90 es una excelente opción."
        ])
    
    if len(productos_actuales) == 0:
        sugerencias.extend([
            "¡Bienvenido a KFC! Te recomiendo nuestros especiales de Miércoles de KFC.",
            "¿Qué te parece nuestro MDK 6 Piezas Combo? ¡El favorito de nuestros clientes!"
        ])
    
    return {
        "tiene_solo_piezas": tiene_solo_piezas,
        "tiene_combo": tiene_combo,
        "sugerencias": sugerencias,
        "mensaje": "¿Te gustaría agregar algo más a tu pedido KFC?"
    }


def finalizar_pedido_kfc_tool(session_id: str) -> Dict[str, Any]:
    """
    Finalizar el pedido KFC y preparar los datos para procesar.

    Args:
        session_id: ID de la sesión del cliente

    Returns:
        Datos del pedido para procesar
    """
    logger.info(f"Finalizando pedido KFC - Session: {session_id}")
    
    if session_id not in pedidos_en_proceso:
        return {
            "error": "No hay pedido para finalizar",
            "mensaje": "Primero necesitas agregar productos a tu pedido"
        }
    
    pedido = pedidos_en_proceso[session_id]
    
    if not pedido["items"]:
        return {
            "error": "Pedido vacío",
            "mensaje": "No hay productos en el pedido para finalizar"
        }
    
    # Preparar orderItems para finalizeOrder
    order_items = []
    for item in pedido["items"]:
        order_items.append({
            "productName": item["producto"],
            "productBase": item["producto_base"],
            "attributes": item.get("atributos", {}),
            "quantity": item["cantidad"],
            "sku": item.get("sku", ""),
            "unitPrice": item["precio_unitario"]
        })
    
    # Limpiar el pedido después de finalizar
    del pedidos_en_proceso[session_id]
    
    return {
        "success": True,
        "orderItems": order_items,
        "total": pedido["total"],
        "resumen_pedido": pedido,
        "mensaje": "Pedido KFC listo para procesar"
    }


def limpiar_pedido_tool(session_id: str) -> Dict[str, Any]:
    """
    Limpiar/cancelar el pedido actual y selecciones pendientes.

    Args:
        session_id: ID de la sesión del cliente

    Returns:
        Confirmación de limpieza
    """
    logger.info(f"Limpiando pedido KFC - Session: {session_id}")
    
    # Limpiar pedido
    pedido_limpiado = False
    if session_id in pedidos_en_proceso:
        del pedidos_en_proceso[session_id]
        pedido_limpiado = True
    
    # Limpiar selecciones pendientes
    seleccion_limpiada = False
    if session_id in selecciones_pendientes:
        del selecciones_pendientes[session_id]
        seleccion_limpiada = True
    
    if pedido_limpiado or seleccion_limpiada:
        return {"success": True, "mensaje": "Tu pedido ha sido cancelado exitosamente"}
    
    return {"success": True, "mensaje": "No había pedido para cancelar"}


def calcular_precio_productos_kfc_tool(productos: List[str]) -> Dict[str, Any]:
    """
    Calcular el precio total de una lista de productos KFC.

    Args:
        productos: Lista de nombres de productos

    Returns:
        Cálculo de precios individuales y total
    """
    logger.info(f"Calculando precios KFC para productos: {productos}")
    
    resultados = []
    total = 0.0
    
    for producto in productos:
        precio = None
        categoria_encontrada = None
        sku = None
        
        for categoria, items in KFC_MENU.items():
            if producto in items:
                precio = items[producto]["precio"]
                categoria_encontrada = categoria
                sku = items[producto]["sku"]
                break
        
        if precio is not None:
            resultados.append({
                "producto": producto,
                "categoria": categoria_encontrada,
                "precio": precio,
                "sku": sku,
                "precio_formateado": f"S/ {precio:.2f}"
            })
            total += precio
        else:
            resultados.append({
                "producto": producto,
                "error": "Producto no encontrado en menú KFC"
            })
    
    return {
        "productos": resultados,
        "total": total,
        "total_formateado": f"S/ {total:.2f}"
    }


def finalize_order_tool(order_items: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Procesar el pedido final de KFC.

    Args:
        order_items: Lista de items del pedido con formato extendido para KFC

    Returns:
        Resultado del procesamiento del pedido
    """
    import random
    import time
    
    logger.info(f"Procesando pedido final KFC con items: {order_items}")
    
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
        order_id = f"KFC-{random.randint(100000, 999999)}"
        total_items = sum(item["quantity"] for item in order_items)
        
        logger.info(f"Pedido KFC procesado exitosamente - ID: {order_id}")
        
        return {
            "status": "SUCCESS",
            "orderId": order_id,
            "message": "¡Pedido KFC procesado exitosamente!",
            "items": order_items,
            "totalItems": total_items,
            "estimatedTime": "20-25 minutos",
            "restaurant": "KFC"
        }
    else:
        logger.warning("Simulando error en procesamiento de pedido KFC")
        
        return {
            "status": "ERROR",
            "error": "Error en el sistema de pedidos KFC",
            "message": "Por favor intenta nuevamente en unos momentos"
        }
