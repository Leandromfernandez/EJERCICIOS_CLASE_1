"""Ejercicio 1:
Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su
sueldo para esa persona."""


nombre = input('Ingrese un nombre: ')
sueldo = input('Ingrese sueldo: ')
sueldo = float(sueldo)
incremento = 0.10
sueldo_total = sueldo + sueldo * incremento
print(f'{nombre} Gana: ${sueldo} y el sueldo con el incremento es: ${sueldo_total}')