import logging
from typing import List, Dict, Any, Optional

# Configurar logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# Menú de Carl's Jr Peru
CARLS_JR_MENU = {
    "PROMOCIONES_Y_PACKS": {
        "BBQ Pack": {
            "nombre_completo": "BBQ Pack",
            "descripcion": "Hamburguesa con carne 100% grelhada con molho BBQ, queijo americano, cebola e picles. Acompanha batatas e Chicken Stars (4 unidades)",
            "precio": 8.90,
            "sku": "PACK001",
            "categoria": "pack",
            "atributos_requeridos": {}
        },
        "Big Star Pack": {
            "nombre_completo": "Big Star Pack",
            "descripcion": "1 Famous Star Burger + 1 Big Carl Burger + 2 batatas médias",
            "precio": 17.90,
            "sku": "PACK002",
            "categoria": "pack",
            "atributos_requeridos": {}
        },
        "Pesto Pack": {
            "nombre_completo": "Pesto Pack",
            "descripcion": "2 Pesto Burgers + 2 batatas médias",
            "precio": 15.00,
            "sku": "PACK003",
            "categoria": "pack",
            "atributos_requeridos": {}
        }
    },
    "HAMBURGUESAS_A_LA_PARRILLA": {
        "Famous Star con Queso": {
            "nombre_completo": "Famous Star con Queso",
            "descripcion": "Nuestra hamburguesa estrella con carne a la parrilla, queso americano, lechuga, tomate y salsa especial",
            "precio": 5.40,
            "sku": "HAM001",
            "categoria": "hamburguesa",
            "atributos_requeridos": {
                "punto_coccion": {
                    "nombre": "¿Cómo la quieres?",
                    "opciones": {
                        "Medio": {"id": "PT001", "descripcion": "Término medio, jugosa"},
                        "Tres Cuartos": {"id": "PT002", "descripcion": "Bien cocida pero jugosa"},
                        "Bien Cocida": {"id": "PT003", "descripcion": "Completamente cocida"}
                    }
                }
            }
        },
        "Big Carl": {
            "nombre_completo": "Hamburguesa Big Carl",
            "descripcion": "Hamburguesa tamaño grande con carne premium a la parrilla",
            "precio": 7.10,
            "sku": "HAM002",
            "categoria": "hamburguesa",
            "atributos_requeridos": {
                "punto_coccion": {
                    "nombre": "¿Cómo la quieres?",
                    "opciones": {
                        "Medio": {"id": "PT001", "descripcion": "Término medio, jugosa"},
                        "Tres Cuartos": {"id": "PT002", "descripcion": "Bien cocida pero jugosa"},
                        "Bien Cocida": {"id": "PT003", "descripcion": "Completamente cocida"}
                    }
                }
            }
        },
        "Western Bacon": {
            "nombre_completo": "Western Bacon Burger",
            "descripcion": "Hamburguesa con bacon crujiente y salsa BBQ",
            "precio": 6.10,
            "sku": "HAM003",
            "categoria": "hamburguesa",
            "atributos_requeridos": {
                "punto_coccion": {
                    "nombre": "¿Cómo la quieres?",
                    "opciones": {
                        "Medio": {"id": "PT001", "descripcion": "Término medio, jugosa"},
                        "Tres Cuartos": {"id": "PT002", "descripcion": "Bien cocida pero jugosa"},
                        "Bien Cocida": {"id": "PT003", "descripcion": "Completamente cocida"}
                    }
                }
            }
        },
        "Hamburguesa Súper Star con Queso": {
            "nombre_completo": "Súper Star con Queso",
            "descripcion": "Version súper de nuestra Famous Star con doble carne",
            "precio": 7.10,
            "sku": "HAM004",
            "categoria": "hamburguesa",
            "atributos_requeridos": {
                "punto_coccion": {
                    "nombre": "¿Cómo la quieres?",
                    "opciones": {
                        "Medio": {"id": "PT001", "descripcion": "Término medio, jugosa"},
                        "Tres Cuartos": {"id": "PT002", "descripcion": "Bien cocida pero jugosa"},
                        "Bien Cocida": {"id": "PT003", "descripcion": "Completamente cocida"}
                    }
                }
            }
        },
        "Hamburguesa Doble Western Bacon": {
            "nombre_completo": "Doble Western Bacon",
            "descripcion": "Doble carne con bacon crujiente y salsa BBQ",
            "precio": 8.00,
            "sku": "HAM005",
            "categoria": "hamburguesa",
            "atributos_requeridos": {
                "punto_coccion": {
                    "nombre": "¿Cómo la quieres?",
                    "opciones": {
                        "Medio": {"id": "PT001", "descripcion": "Término medio, jugosa"},
                        "Tres Cuartos": {"id": "PT002", "descripcion": "Bien cocida pero jugosa"},
                        "Bien Cocida": {"id": "PT003", "descripcion": "Completamente cocida"}
                    }
                }
            }
        },
        "Hamburguesa Teriyaki": {
            "nombre_completo": "Hamburguesa Teriyaki",
            "descripcion": "Hamburguesa con salsa teriyaki dulce",
            "precio": 5.90,
            "sku": "HAM006",
            "categoria": "hamburguesa",
            "atributos_requeridos": {
                "punto_coccion": {
                    "nombre": "¿Cómo la quieres?",
                    "opciones": {
                        "Medio": {"id": "PT001", "descripcion": "Término medio, jugosa"},
                        "Tres Cuartos": {"id": "PT002", "descripcion": "Bien cocida pero jugosa"},
                        "Bien Cocida": {"id": "PT003", "descripcion": "Completamente cocida"}
                    }
                }
            }
        }
    },
    "ANGUS_MEGA_BURGER": {
        "Original Angus Burger": {
            "nombre_completo": "Original Angus Burger",
            "descripcion": "Hamburguesa premium con carne Angus de alta calidad",
            "precio": 6.80,
            "sku": "ANG001",
            "categoria": "angus",
            "atributos_requeridos": {
                "punto_coccion": {
                    "nombre": "¿Cómo la quieres?",
                    "opciones": {
                        "Medio": {"id": "PT001", "descripcion": "Término medio, jugosa"},
                        "Tres Cuartos": {"id": "PT002", "descripcion": "Bien cocida pero jugosa"},
                        "Bien Cocida": {"id": "PT003", "descripcion": "Completamente cocida"}
                    }
                }
            }
        },
        "Famous Star Mega Angus Burger": {
            "nombre_completo": "Famous Star Mega Angus",
            "descripcion": "Nuestra Famous Star con carne Angus premium",
            "precio": 6.80,
            "sku": "ANG002",
            "categoria": "angus",
            "atributos_requeridos": {
                "punto_coccion": {
                    "nombre": "¿Cómo la quieres?",
                    "opciones": {
                        "Medio": {"id": "PT001", "descripcion": "Término medio, jugosa"},
                        "Tres Cuartos": {"id": "PT002", "descripcion": "Bien cocida pero jugosa"},
                        "Bien Cocida": {"id": "PT003", "descripcion": "Completamente cocida"}
                    }
                }
            }
        },
        "Western Bacon Cheese Angus Mega Burger": {
            "nombre_completo": "Western Bacon Cheese Angus Mega",
            "descripcion": "Angus con bacon crujiente y queso",
            "precio": 7.50,
            "sku": "ANG003",
            "categoria": "angus",
            "atributos_requeridos": {
                "punto_coccion": {
                    "nombre": "¿Cómo la quieres?",
                    "opciones": {
                        "Medio": {"id": "PT001", "descripcion": "Término medio, jugosa"},
                        "Tres Cuartos": {"id": "PT002", "descripcion": "Bien cocida pero jugosa"},
                        "Bien Cocida": {"id": "PT003", "descripcion": "Completamente cocida"}
                    }
                }
            }
        }
    },
    "FRANGO": {
        "Chicken Tenders 3 pzas": {
            "nombre_completo": "Chicken Tenders (3 piezas)",
            "descripcion": "3 tiras de pollo empanizado y crujiente",
            "precio": 4.80,
            "sku": "CHK001",
            "categoria": "pollo",
            "atributos_requeridos": {
                "salsa": {
                    "nombre": "¿Qué salsa prefieres?",
                    "opciones": {
                        "Honey Mustard": {"id": "SAL001", "descripcion": "Miel con mostaza"},
                        "Buttermilk Ranch": {"id": "SAL002", "descripcion": "Salsa ranch cremosa"},
                        "BBQ": {"id": "SAL003", "descripcion": "Salsa barbacoa"}
                    }
                }
            }
        },
        "Chicken Tenders 5 pzas": {
            "nombre_completo": "Chicken Tenders (5 piezas)",
            "descripcion": "5 tiras de pollo empanizado y crujiente",
            "precio": 7.00,
            "sku": "CHK002",
            "categoria": "pollo",
            "atributos_requeridos": {
                "salsa": {
                    "nombre": "¿Qué salsa prefieres?",
                    "opciones": {
                        "Honey Mustard": {"id": "SAL001", "descripcion": "Miel con mostaza"},
                        "Buttermilk Ranch": {"id": "SAL002", "descripcion": "Salsa ranch cremosa"},
                        "BBQ": {"id": "SAL003", "descripcion": "Salsa barbacoa"}
                    }
                }
            }
        },
        "Chicken Stars 6 pzas": {
            "nombre_completo": "Chicken Stars (6 piezas)",
            "descripcion": "6 nuggets de pollo en forma de estrella",
            "precio": 3.30,
            "sku": "CHK003",
            "categoria": "pollo",
            "atributos_requeridos": {}
        },
        "Bacon Swiss Crispy Sandwich": {
            "nombre_completo": "Bacon Swiss Crispy Sandwich",
            "descripcion": "Sándwich de pollo crispy con bacon y queso suizo",
            "precio": 5.40,
            "sku": "CHK004",
            "categoria": "pollo",
            "atributos_requeridos": {}
        }
    },
    "COMBOS": {
        "Combo Famous Star": {
            "nombre_completo": "Combo Famous Star con Queso",
            "descripcion": "Famous Star + papas + bebida",
            "precio": 8.90,
            "sku": "CMB001",
            "categoria": "combo",
            "atributos_requeridos": {
                "punto_coccion": {
                    "nombre": "¿Cómo quieres la hamburguesa?",
                    "opciones": {
                        "Medio": {"id": "PT001", "descripcion": "Término medio, jugosa"},
                        "Tres Cuartos": {"id": "PT002", "descripcion": "Bien cocida pero jugosa"},
                        "Bien Cocida": {"id": "PT003", "descripcion": "Completamente cocida"}
                    }
                },
                "acompanamiento": {
                    "nombre": "¿Qué papas prefieres?",
                    "opciones": {
                        "Papas Normales": {"id": "ACP001", "descripcion": "Papas fritas clásicas"},
                        "Crisscut Fries": {"id": "ACP002", "descripcion": "Papas en forma de rejilla"},
                        "Onion Rings": {"id": "ACP003", "descripcion": "Aros de cebolla"}
                    }
                },
                "bebida": {
                    "nombre": "¿Qué bebida quieres?",
                    "opciones": {
                        "Coca-Cola": {"id": "BEB001", "descripcion": "Coca-Cola clásica"},
                        "Fanta": {"id": "BEB002", "descripcion": "Fanta naranja"},
                        "Sprite": {"id": "BEB003", "descripcion": "Sprite lima-limón"}
                    }
                }
            }
        },
        "Combo Big Carl": {
            "nombre_completo": "Combo Big Carl",
            "descripcion": "Big Carl + papas + bebida",
            "precio": 10.60,
            "sku": "CMB002",
            "categoria": "combo",
            "atributos_requeridos": {
                "punto_coccion": {
                    "nombre": "¿Cómo quieres la hamburguesa?",
                    "opciones": {
                        "Medio": {"id": "PT001", "descripcion": "Término medio, jugosa"},
                        "Tres Cuartos": {"id": "PT002", "descripcion": "Bien cocida pero jugosa"},
                        "Bien Cocida": {"id": "PT003", "descripcion": "Completamente cocida"}
                    }
                },
                "acompanamiento": {
                    "nombre": "¿Qué papas prefieres?",
                    "opciones": {
                        "Papas Normales": {"id": "ACP001", "descripcion": "Papas fritas clásicas"},
                        "Crisscut Fries": {"id": "ACP002", "descripcion": "Papas en forma de rejilla"},
                        "Onion Rings": {"id": "ACP003", "descripcion": "Aros de cebolla"}
                    }
                },
                "bebida": {
                    "nombre": "¿Qué bebida quieres?",
                    "opciones": {
                        "Coca-Cola": {"id": "BEB001", "descripcion": "Coca-Cola clásica"},
                        "Fanta": {"id": "BEB002", "descripcion": "Fanta naranja"},
                        "Sprite": {"id": "BEB003", "descripcion": "Sprite lima-limón"}
                    }
                }
            }
        },
        "Combo Buttermilk Ranch": {
            "nombre_completo": "Combo Buttermilk Ranch",
            "descripcion": "Chicken sandwich con salsa ranch + papas + bebida",
            "precio": 8.69,
            "sku": "CMB003",
            "categoria": "combo",
            "atributos_requeridos": {
                "acompanamiento": {
                    "nombre": "¿Qué papas prefieres?",
                    "opciones": {
                        "Papas Normales": {"id": "ACP001", "descripcion": "Papas fritas clásicas"},
                        "Crisscut Fries": {"id": "ACP002", "descripcion": "Papas en forma de rejilla"},
                        "Onion Rings": {"id": "ACP003", "descripcion": "Aros de cebolla"}
                    }
                },
                "bebida": {
                    "nombre": "¿Qué bebida quieres?",
                    "opciones": {
                        "Coca-Cola": {"id": "BEB001", "descripcion": "Coca-Cola clásica"},
                        "Fanta": {"id": "BEB002", "descripcion": "Fanta naranja"},
                        "Sprite": {"id": "BEB003", "descripcion": "Sprite lima-limón"}
                    }
                }
            }
        }
    }
}

# Variable global para almacenar pedidos en construcción y selecciones pendientes
pedidos_en_proceso = {}
selecciones_pendientes = {}


def consultar_menu_carls_jr_tool(categoria: Optional[str] = None) -> Dict[str, Any]:
    """
    Consultar el menú completo de Carl's Jr o por categoría específica.

    Args:
        categoria: Categoría específica (PROMOCIONES_Y_PACKS, HAMBURGUESAS_A_LA_PARRILLA, ANGUS_MEGA_BURGER, FRANGO, COMBOS)

    Returns:
        Información del menú Carl's Jr
    """
    logger.info(f"Consultando menú Carl's Jr - categoría: {categoria}")
    
    if categoria and categoria.upper() in CARLS_JR_MENU:
        return {
            "categoria": categoria.upper(),
            "productos": CARLS_JR_MENU[categoria.upper()],
            "mensaje": f"Aquí tienes los productos de {categoria.replace('_', ' ').title()}"
        }
    
    return {
        "menu_completo": CARLS_JR_MENU,
        "categorias": ["PROMOCIONES_Y_PACKS", "HAMBURGUESAS_A_LA_PARRILLA", "ANGUS_MEGA_BURGER", "FRANGO", "COMBOS"],
        "mensaje": "¡Bienvenido a Carl's Jr! Estas son nuestras deliciosas hamburguesas a la parrilla"
    }


def iniciar_seleccion_producto_tool(session_id: str, nombre_producto: str) -> Dict[str, Any]:
    """
    Iniciar el proceso de selección de un producto Carl's Jr con sus atributos.

    Args:
        session_id: ID de la sesión del cliente
        nombre_producto: Nombre del producto Carl's Jr a configurar

    Returns:
        Primera pregunta sobre atributos o confirmación si no requiere atributos
    """
    logger.info(f"Iniciando selección de producto - Session: {session_id}, Producto: {nombre_producto}")
    
    # Buscar el producto en el menú
    producto_encontrado = None
    categoria_producto = None
    
    for categoria, productos in CARLS_JR_MENU.items():
        if nombre_producto in productos:
            producto_encontrado = productos[nombre_producto]
            categoria_producto = categoria
            break
    
    if not producto_encontrado:
        return {"error": f"Producto '{nombre_producto}' no encontrado en el menú Carl's Jr"}
    
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
        "mensaje": f"¡Perfecto! Has elegido {nombre_producto} por ${producto_encontrado['precio']:.2f}. Ahora necesito que elijas: {atributo_info['nombre']}"
    }


def seleccionar_atributo_tool(session_id: str, atributo: str, valor: str) -> Dict[str, Any]:
    """
    Seleccionar un valor para un atributo del producto en configuración.

    Args:
        session_id: ID de la sesión del cliente
        atributo: Nombre del atributo (punto_coccion, acompanamiento, bebida, salsa)
        valor: Valor seleccionado para el atributo

    Returns:
        Siguiente pregunta de atributo o confirmación final
    """
    logger.info(f"Seleccionando atributo - Session: {session_id}, Atributo: {atributo}, Valor: {valor}")
    
    if session_id not in selecciones_pendientes:
        return {"error": "No hay producto en selección. Primero elige un producto."}
    
    seleccion = selecciones_pendientes[session_id]
    producto_info = CARLS_JR_MENU[seleccion["categoria"]][seleccion["producto"]]
    
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


def sugerir_complementos_carls_jr_tool(productos_actuales: List[str]) -> Dict[str, Any]:
    """
    Sugerir productos adicionales basados en el pedido actual de Carl's Jr.

    Args:
        productos_actuales: Lista de productos ya en el pedido

    Returns:
        Sugerencias de productos adicionales
    """
    logger.info(f"Generando sugerencias Carl's Jr para productos: {productos_actuales}")
    
    tiene_hamburguesa_individual = any("Famous Star" in prod or "Big Carl" in prod or "Western" in prod for prod in productos_actuales if "Combo" not in prod)
    tiene_combo = any("Combo" in prod for prod in productos_actuales)
    tiene_pack = any("Pack" in prod for prod in productos_actuales)
    tiene_angus = any("Angus" in prod for prod in productos_actuales)
    
    sugerencias = []
    
    if tiene_hamburguesa_individual and not tiene_combo:
        sugerencias.extend([
            "¿Te gustaría convertir tu hamburguesa en combo? ¡Incluye papas y bebida por solo $3.50 más!",
            "¿Qué tal agregar unas Crisscut Fries? Son nuestras papas especiales en forma de rejilla."
        ])
    
    if not tiene_combo and not tiene_hamburguesa_individual and not tiene_pack:
        sugerencias.extend([
            "Te recomiendo nuestro Combo Famous Star por $8.90 - ¡hamburguesa + papas + bebida!",
            "¿O prefieres probar el BBQ Pack por $8.90? Incluye hamburguesa, papas y Chicken Stars.",
            "Para algo premium, prueba el Big Carl por $7.10 - ¡nuestra hamburguesa más grande!"
        ])
    
    if tiene_combo and not tiene_angus:
        sugerencias.extend([
            "¿Te gustaría probar nuestras hamburguesas Angus premium? Son con carne de mayor calidad.",
            "¿Qué tal agregar Chicken Stars como acompañamiento? Son perfectos para compartir."
        ])
    
    if len(productos_actuales) == 0:
        sugerencias.extend([
            "¡Bienvenido a Carl's Jr! Te recomiendo nuestra Famous Star con Queso - ¡nuestra hamburguesa estrella!",
            "¿Qué te parece nuestro BBQ Pack? Es una excelente oferta completa por $8.90.",
            "Si tienes mucha hambre, el Big Carl es perfecto - ¡nuestra hamburguesa más grande!"
        ])
    
    return {
        "tiene_hamburguesa_individual": tiene_hamburguesa_individual,
        "tiene_combo": tiene_combo,
        "tiene_pack": tiene_pack,
        "tiene_angus": tiene_angus,
        "sugerencias": sugerencias,
        "mensaje": "¿Te gustaría agregar algo más a tu pedido Carl's Jr?"
    }


def finalizar_pedido_carls_jr_tool(session_id: str) -> Dict[str, Any]:
    """
    Finalizar el pedido Carl's Jr y preparar los datos para procesar.

    Args:
        session_id: ID de la sesión del cliente

    Returns:
        Datos del pedido para procesar
    """
    logger.info(f"Finalizando pedido Carl's Jr - Session: {session_id}")
    
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
        "mensaje": "Pedido Carl's Jr listo para procesar"
    }


def limpiar_pedido_tool(session_id: str) -> Dict[str, Any]:
    """
    Limpiar/cancelar el pedido actual y selecciones pendientes.

    Args:
        session_id: ID de la sesión del cliente

    Returns:
        Confirmación de limpieza
    """
    logger.info(f"Limpiando pedido Carl's Jr - Session: {session_id}")
    
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


def calcular_precio_productos_carls_jr_tool(productos: List[str]) -> Dict[str, Any]:
    """
    Calcular el precio total de una lista de productos Carl's Jr.

    Args:
        productos: Lista de nombres de productos

    Returns:
        Cálculo de precios individuales y total
    """
    logger.info(f"Calculando precios Carl's Jr para productos: {productos}")
    
    resultados = []
    total = 0.0
    
    for producto in productos:
        precio = None
        categoria_encontrada = None
        sku = None
        
        for categoria, items in CARLS_JR_MENU.items():
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
                "precio_formateado": f"${precio:.2f}"
            })
            total += precio
        else:
            resultados.append({
                "producto": producto,
                "error": "Producto no encontrado en menú Carl's Jr"
            })
    
    return {
        "productos": resultados,
        "total": total,
        "total_formateado": f"${total:.2f}"
    }


def finalize_order_tool(order_items: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Procesar el pedido final de Carl's Jr.

    Args:
        order_items: Lista de items del pedido con formato extendido para Carl's Jr

    Returns:
        Resultado del procesamiento del pedido
    """
    import random
    import time
    
    logger.info(f"Procesando pedido final Carl's Jr con items: {order_items}")
    
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
        order_id = f"CJR-{random.randint(100000, 999999)}"
        total_items = sum(item["quantity"] for item in order_items)
        
        logger.info(f"Pedido Carl's Jr procesado exitosamente - ID: {order_id}")
        
        return {
            "status": "SUCCESS",
            "orderId": order_id,
            "message": "¡Pedido Carl's Jr procesado exitosamente!",
            "items": order_items,
            "totalItems": total_items,
            "estimatedTime": "15-20 minutos",
            "restaurant": "Carl's Jr"
        }
    else:
        logger.warning("Simulando error en procesamiento de pedido Carl's Jr")
        
        return {
            "status": "ERROR",
            "error": "Error en el sistema de pedidos Carl's Jr",
            "message": "Por favor intenta nuevamente en unos momentos"
        }
