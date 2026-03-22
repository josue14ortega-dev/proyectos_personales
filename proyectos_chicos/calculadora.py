"""
CALCULADORA CON PYTHON
    Holaa, este es un mini proyecto en el cual hago una calculadora
    con python con el objetivo de afinar mis habilidades y logica.
Nombre: Josue
Fecha: 21-Marzo-2026
"""


num1 = float(input('Ponga un numero: '))
num2 = float(input('Ponga un numero: '))

print('1. Suma')
print('2. Resta')
print('3. Multiplicacion')
print('4. Division')

opcion = input('Escribe un numero de la opcion (1/2/3/4): ')

resultado = 0
if opcion == '1':
    resultado = num1 + num2
elif opcion == '2':
    resultado = num1 - num2
elif opcion == '3':
    resultado = num1 * num2
elif opcion == '4':
    
    if num2 == 0:
        print('Nose puede dividir el 0')
    else:
        resultado = num1 / num2
        
else:
    print('Opcion no valida')
    
print(f'El resultado es: {resultado}')
