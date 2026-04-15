"""
Generador y Administrador de Contraseñas Seguro
Nombre: Josue Ortega
Fecha: 05-Abril-2026
"""

import random as r
import string as st

letras_minus = st.ascii_lowercase
letras_manus = st.ascii_uppercase
num = st.digits
simbolos =st.punctuation

caracteres = letras_minus + letras_manus + num + simbolos

password = ""


sitio = input("¿Para que sitio es tu contraseña?: ")
largo = int(input("¿De que largo va a ser tu contraseña?: "))

for i in range(largo):
    caracter_elegido =r.choice(caracteres)
    password += caracter_elegido
    
password_cifrado = ""
desplazamiento = 3

for letra in password:
    nueva_letra = chr(ord(letra) + desplazamiento)
    password_cifrado += nueva_letra
    
        
print(f"Tu contraseña real para {sitio} es: {password}")

with open("Mis_contraseñas.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"Sitio: {sitio} | Password: {password_cifrado}\n") 

print("\n--- Recuperando datos del archivo ---")

with open("Mis_contraseñas.txt", "r", encoding="utf-8") as archivo_lectura: 
    lineas = archivo_lectura.readlines()
    ultima_linea = lineas[-1]
    print(f"Dato cifrado en el archivo: {ultima_linea.strip()}")
    
pass_a_descifrar = password_cifrado
desplazamiento = 3
password_final = ""

for letra in pass_a_descifrar:
    numero = ord(letra) - desplazamiento
    password_final += chr(numero)
print(f"Contraseña recuperada y descifrada: {password_final}")

buscar_password = input("Nombre del sitio a buscar: ")
for linea in lineas:
    if buscar_password.lower() in linea.lower():
        partes = linea.split("|")
        pass_limpia = partes[1].replace(" Password: ", "").strip()
        
        password_final = "" 
        
        for character in pass_limpia:
            password_final += chr(ord(character) - 3)
            
        print(f"Lo encontre! La contraseña es: {password_final}")
        break
        
        
    