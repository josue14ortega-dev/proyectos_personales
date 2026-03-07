""" Automatizacion de Sheets
Nombre: Josue
Fecha: 6-Marzo-2026
"""


import pandas as pd

df = pd.read_csv("ventas - Hoja 1.csv")

def calcular_ajuste(precio):
    if precio < 50:
        return precio * 0.15
    else:
        return 0


df['Aumento'] = df['Precio'].apply(calcular_ajuste)


total_ganancia = df['Aumento'].sum()

df.to_csv('reporte_final_sheets.csv', index=False)

print(f"¡Hecho! Se procesaron {len(df)} productos.")
print(f"La ganancia extra total es de: ${total_ganancia:.2f}")

import matplotlib.pyplot as plt

# 1. Preparar los datos para el gráfico
nombres_productos = df['Producto']
aumentos = df['Aumento']

colores_inteligentes = ["limegreen" if a > 0 else "lightgrey" for a in df["Aumento"] ]

# 2. Crear el gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(nombres_productos, aumentos, color='skyblue')

# 3. Personalizarlo (Esto es lo que el cliente valora)
plt.title('Impacto Económico por Producto')
plt.xlabel('Productos')
plt.ylabel('Ganancia Extra ($)')
plt.xticks(rotation=45) # Rota los nombres para que se lean bien

# 4. Guardar la imagen
plt.tight_layout()
plt.savefig('REPORTE DE OPTIMIZACIÓN FINANCIERA.png')
print("¡Gráfico generado con éxito como 'REPORTE DE OPTIMIZACIÓN FINANCIERA.png'!")