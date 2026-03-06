import pandas as pd

# 1. Cargar los datos del CSV que bajaste de Sheets
df = pd.read_csv("ventas - Hoja 1.csv")
# 2. Tu lógica de ayer aplicada a una columna entera
# Vamos a crear una columna nueva llamada 'Aumento'
def calcular_ajuste(precio):
    if precio < 50:
        return precio * 0.15
    else:
        return 0

# Aplicamos la función a la columna 'Precio'
df['Aumento'] = df['Precio'].apply(calcular_ajuste)

# 3. Calcular la ganancia total para el reporte
total_ganancia = df['Aumento'].sum()

# 4. Guardar el resultado en un nuevo Excel/CSV
df.to_csv('reporte_final_sheets.csv', index=False)

print(f"¡Hecho! Se procesaron {len(df)} productos.")
print(f"La ganancia extra total es de: ${total_ganancia:.2f}")