""" Simulador de descuentos
fecha: 03-Marzo-2026
Nombre: Josue
"""
productos = {
    "Audifonos": {"costo": 20, "precio": 45},
    "Cargador": {"costo": 10, "precio": 18},
    "Funda": {"costo": 5, "precio": 15},
}
def simular_descuento(productos, porcentaje):
    
    for nombre, datos in productos.items():
        # 1. Calcula el precio con descuento (ej: si es 10%, multiplica por 0.90)
        descuento = 1 - (porcentaje / 100)
        # 2. Calcula la nueva ganancia
        precio_oferta = datos["precio"] * descuento
        # 3. Usa el IF para ver si el negocio sigue siendo sano
        nueva_ganancia =  precio_oferta - datos["costo"]
        
       
        if nueva_ganancia < 0:
           print(f"❌ ¡ALERTA! {nombre}: Perderías ${abs(nueva_ganancia)} por cada venta.")
        else:
            print(f"✅ {nombre}: Nueva ganancia: ${nueva_ganancia:.2f}")
simular_descuento(productos, 60)