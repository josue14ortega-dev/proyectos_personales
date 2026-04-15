'''
Simulador de Metas Financieras con Interés Compuesto
Este es un script desarrollado en Python diseñado para calcular 
el tiempo necesario para alcanzar una meta de ahorro específica, 
considerando rendimientos diarios y capitalización de intereses 
(interés compuesto).
nombre: Josue
fecha. 01-Abril-2026
'''

saldo_actual = float(input('ingrese el saldo que tienes hoy: '))
tasa_anual = float(input('Cual es su tasa anual en su banco: '))
meta = float(input('¿Cual es el precio? '))

tasa_diaria = (tasa_anual / 100) / 365
if tasa_anual <= 0:
    print('La tasa anual debe ser mayor a 0')
else:
    dias = 0
    while saldo_actual < meta:
        ganancia = saldo_actual * (tasa_diaria)
        saldo_actual += ganancia
        dias += 1
    meses = dias // 30
    dias_restantes = dias % 30
    print(f'Josue, te faltan {meses} meses y { dias} dias ')