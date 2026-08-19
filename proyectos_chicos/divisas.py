"""
CALCULADORA DE DIVISAS
    Holaa, este es un mini proyecto en el cual hago una calculadora
    de divisas con python con el objetivo de afinar mis habilidades y logica.
Nombre: Josue
Fecha: 27-Marzo-2026
"""
pregunta = float(input('¿A cuanto esta el dolar hoy? '))
VALOR_USD = pregunta 
print('1. Dolares')
print('2. Pesos')

cambio = input('Escribe un numero (1/2): ')
cantidad = float(input('Cantidad que desea convertir: '))

resultado = 0
if cambio == '1':
    resultado = cantidad * VALOR_USD
    
    
elif cambio =='2':
    resultado = cantidad/VALOR_USD
    
    
else:
    print('Resultado invalido')
    

print(f'El resultado es: {resultado:.2f}')
    
    