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
    while numero == 0:
        numero = input('Error. Ingrese un numero: ')
        numero = int(numero)

    lista_numeros.append(numero)      
    contador += 1

print(f'lista de numeros: {lista_numeros}')
########################################################### 
contador_pares = 0
flag_par = False
contador_impares = 0
suma_positivos = 0
producto_negativo = 1
flag_negativos = False
minimo = None
maximo_pares = None

for numero in lista_numeros:
    #A
    if numero % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1
    #B
    if minimo == None or numero < minimo:
        minimo = numero
    #C
    if numero % 2 == 0:
        if maximo_pares == None or numero > maximo_pares:
            maximo_pares = numero
            flag_par = True
    #D
    if numero > 0:
        suma_positivos = suma_positivos + numero
    #E
    if numero < 0:
        producto_negativo = producto_negativo * numero
        flag_negativos = True

###########################################################
#SE MUESTRAN TODOS LOS MENSAJES
#A-
print(f'hay: {contador_impares} numeros impares\n hay: {contador_pares} numeros pares')

#B-
print(f'El menor de los numeros ingresados es: {minimo}')

#C-
if flag_par == True:
    print(f'El mayor de los numero pares es: {maximo_pares}')
else:
    print(f'No hay numeros pares')

#D-    
print(f'la suma total de los positivos es: {suma_positivos}')

#E-
if flag_negativos == True:
    print(f'El producto de los numero negativos es: {producto_negativo}')
else:
    print('No hay numeros negativos.')

##################################################################

