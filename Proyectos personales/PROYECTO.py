# Diccionario de productos: cada producto tiene costo y precio
# Nombre: Josue
# Fecha: 02-Marzo-2026
productos = {
    "Audifonos": {"costo": 20, "precio": 45},
    "Cargador": {"costo": 10, "precio": 18},
    "Funda": {"costo": 5, "precio": 15},
}


def ganancia_por_producto(productos):
    """Devuelve la ganancia (precio - costo) de cada producto."""
    for nombres, datos in productos.items():
        ganancia = datos["precio"]- datos ["costo"]
        print(f"La ganancia de {nombres} es: ${ganancia}")


def ganancia_total(productos):
    """Devuelve la suma de todas las ganancias."""
    total= 0
    for nombres, datos in productos.items():
        ganancia_actual = datos["precio"]- datos["costo"]
        total += ganancia_actual
    return total
resultado= ganancia_total(productos)
print(f"La ganancia total del negocio es: ${resultado}")

def producto_mas_rentable(productos):
    """Devuelve el nombre del producto con mayor ganancia."""
    max_ganancia = 0
    producto_ganador =""
    for nombre,datos in productos.items():
        ganancia_actual = datos["precio"] - datos["costo"]
        
        if ganancia_actual > max_ganancia:
            max_ganancia = ganancia_actual
            producto_ganador= nombre
    return producto_ganador
ganador = producto_mas_rentable(productos)
print(f"El producto estrella es:{ganador}")
