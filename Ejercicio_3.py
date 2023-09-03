"""
Ejercicio 3:
Ingresar 5 números enteros, distintos de cero.
Informar:
a. Cantidad de pares e impares.
b. El menor número ingresado.
c. De los pares el mayor número ingresado.
d. Suma de los positivos.
e. Producto de los negativos."""

contador = 0
lista_numeros = []

while contador < 5:
    numero = input('Ingrese un numero: ')
    numero = int(numero)
    lista_numeros.append(numero)      
    contador += 1

print(f'lista de numeros: {lista_numeros}')
###########################################################
 # A-
contador_pares = 0
contador_impares = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1    
print(f'hay: {contador_impares} numeros impares\n hay: {contador_pares} numeros pares')
###########################################################

# B-
minimo = None
for numero in lista_numeros:
    if minimo == None or numero < minimo:
        minimo = numero    
print(f'El menor de los numeros ingresados es: {minimo}')
###########################################################
maximo_pares = None
for numero in lista_numeros:
    if numero % 2 == 0:
        if maximo_pares == None or numero > maximo_pares:
            maximo_pares = numero
print(f'El mayor de los numero pares es: {maximo_pares}')
###########################################################
# C-
suma_positivos = 0
for numero in lista_numeros:
    if numero > 0:
        suma_positivos = suma_positivos + numero
print(f'la suma total de los positivos es: {suma_positivos}')
###########################################################

# D-
producto_negativo = 1
for numero in lista_numeros:
    if numero < 0:
        producto_negativo = producto_negativo * numero
print(f'El producto de los numero negativos es: {producto_negativo}')



