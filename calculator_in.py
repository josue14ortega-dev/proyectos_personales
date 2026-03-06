""" Calculador de optimizacion de ingresos
Nombre: Josue
Fecha: 4-Marzo-2026
    CONSISTE EN CREAR UN PROGRAMA QUE ANALICE UNA LISTA
    DE PRECIOS Y LE DIGA AL DUÑO DE LA TIENDA CUANTO DINERO 
    GANARA SI SUBE LOS PRECIOS DE SUS PRODUCTOS MAS BARATOS
"""


# Lista de precios actuales en la tienda
precios = [20, 55, 15, 80, 40, 100]
ganancia_extra_total = 0
for precio in precios:
    if precio < 50:
        precio_calculado = precio * 0.15
        ganancia_extra_total += precio_calculado
        print(f"Producto de ${precio}: aumento de ${ganancia_extra_total}")
    else:
        print(f"Producto de ${precio}: se mantiene igual")
    
print(ganancia_extra_total)