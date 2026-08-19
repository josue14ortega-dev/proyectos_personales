import os
import json
import streamlit as st

st.title("Tracker financiero")
def cargar_datos():
    if os.path.exists('finanzas.json'):
        with open('finanzas.json', 'r') as archivo:
            return json.load(archivo)
    else:
        return []
transacciones = cargar_datos()

total_ingresos = 0.0
total_gastos = 0.0
for t in transacciones:
    if t['tipo'] == 'ingreso':
        total_ingresos += t['monto']
    elif t['tipo'] == 'gasto':
        total_gastos += t['monto']
balance = total_ingresos - total_gastos
st.metric(label = 'Ingresos', value = f'${total_ingresos:.2f}')
st.metric(label='Gastos', value = f' ${total_gastos:.2f}')
st.metric(label= 'Balance', value= f'${total_ingresos - total_gastos:.2f}')