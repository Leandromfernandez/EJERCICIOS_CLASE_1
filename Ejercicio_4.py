"""Ejercicio 4:
Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil
distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO
ser soltero.'"""
###########################################################################################

edad = int(input('Ingrese una edad: '))
while edad <= 0:
    edad = int(input('ERROR. Ingrese una edad: '))

estado_civil = input('Ingrese el estado civil: ')
estado_civil = estado_civil.capitalize()
while estado_civil != 'Soltero' and estado_civil != 'Casado':        
    estado_civil = input('ERROR. Ingrese el estado civil: ')
    estado_civil = estado_civil.capitalize()

if edad < 18 and estado_civil != 'Soltero':
    print(f'Es muy pequeño para NO ser soltero')



