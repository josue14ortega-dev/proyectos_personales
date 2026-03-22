import pandas as pd


df = pd.read_csv("contactos.csv")
df["Nombre"] = df['Nombre'].str.strip().str.title()
df['Email'] = df['Email'].str.strip().str.lower()
df['Ciudad'] = df['Ciudad'].str.strip().str.upper()

print(df)
df.to_csv('Contactos_Limpios.csv', index=False)