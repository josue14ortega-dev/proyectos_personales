"""
CALCULADORA CON PYTHON
    Holaa, este es un mini proyecto en el cual hago una calculadora
    con python con el objetivo de afinar mis habilidades y logica.
Nombre: Josue
Fecha: 21-Marzo-2026
"""

#Se añade el float para si un numero tiene decimal, y el input para que el usuario ponga el numero.
num1 = float(input('Ponga un numero: '))
num2 = float(input('Ponga un numero: '))
#Este es el menu de las opciones que hay.
print('1. Suma')
print('2. Resta')
print('3. Multiplicacion')
print('4. Division')
#Aqui esta variable, manda un mensaje y gracias al input se puede seleccionar.
opcion = input('Escribe un numero de la opcion (1/2/3/4): ')
#Dependiendo la eleccion del usuario, se hacedicha operacion, aqui entra en juego los if, elif y else
resultado = 0
if opcion == '1':
    resultado = num1 + num2
elif opcion == '2':
    resultado = num1 - num2
elif opcion == '3':
    resultado = num1 * num2
elif opcion == '4': #Dentro de este else se añade otras condicionales para lograr el resultado adecuado
    if num2 == 0:
        print('Nose puede dividir el 0')
    else:
        resultado = num1 / num2
        
else:
    print('Opcion no valida')
    
print(f'El resultado es: {resultado}')# el f'strings se usa para poder poner los {} sin que haya problema
