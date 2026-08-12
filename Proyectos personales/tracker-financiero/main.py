import json
import os



if os.path.exists('finanzas.json'):
    with open('finanzas.json', 'r') as archivo:
        transacciones = json.load(archivo)
else:
    transacciones = []

while True:
    while True:
        try:
            monto = (float(input('¿Cual es el monto que desea ingresar? ')))
            if monto <=0:
                print("Elemento no valido, ingrese una cantidad")
                continue
            break
        except ValueError:
            print('Elemento no valido')
    while True:    
        tipo =input('Tipo de ingreso(ingreso/gasto): ')
        if tipo in ['ingreso', 'gasto']:
            break
        print("Elemento no valido, coloque ingreso-gasto")
    concepto = input('Concepto o descripcion: ').strip()
    
   

    nueva_transaccion = {
        'monto': monto,
        'tipo': tipo,
        'concepto': concepto
    }
    

    transacciones.append(nueva_transaccion)
    
    while True:
        respuesta = input('¿Desea integrar otra transaccion? (s/n): ')
        if respuesta in ['s' , 'n']:
            break
        print("Respuesta no valida, ingrese 's' o 'n'. ")
    if respuesta == 'n':
            break
    
with open('finanzas.json', 'w') as datos:
    json.dump(transacciones, datos, indent=4)
    
for transaccion in transacciones:
     print(f"Monto:{transaccion['monto']:.2f} -- Concepto:{transaccion['concepto']} -- Tipo:{transaccion['tipo']}")

print(f"\nTotal de transacciones:{len(transacciones)}")


total = 0.0
for transaccion in transacciones:
    if transaccion['tipo'].lower() == 'ingreso':
        total += transaccion['monto']
    else:
        total -= transaccion['monto']
print(f"Saldo final disponible: ${total:.2f}")