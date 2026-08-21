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
def guardar_datos(transacciones):
    with open('finanzas.json', 'w') as archivo:
        json.dump(transacciones, archivo, indent=4)


total_ingresos = 0.0
total_gastos = 0.0
for t in transacciones:
    if t['tipo'] == 'ingreso':
        total_ingresos += t['monto']
    elif t['tipo'] == 'gasto':
        total_gastos += t['monto']
balance = total_ingresos - total_gastos

c1,c2, c3 = st.columns(3)
c1.metric('Ingresos', f'${total_ingresos:.2f}')
c2.metric('Gastos',  f' ${total_gastos:.2f}')
c3.metric('Balance',  f'${total_ingresos - total_gastos:.2f}')

monto =st.number_input('Monto', min_value=0.0, step=10.0)
tipo = st.selectbox("Tipo", ["Ingreso", "Gasto"])
concepto = st.text_input("Concepto:")
fecha = st.date_input("Fecha:")

if st.button("Guardar"):
    nueva_transaccion = {
    'monto': monto,
    'tipo':tipo,
    'concepto':concepto,
    'fecha':str(fecha)
}
    transacciones.append(nueva_transaccion)
    guardar_datos(transacciones)
    st.success('Transaccion hecha!!')

