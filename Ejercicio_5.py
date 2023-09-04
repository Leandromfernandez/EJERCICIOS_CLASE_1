"""Ejercicio 5:
Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
por cada estadía como base, se pide el ingreso de una estación del
año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
Plata/Cordoba) para vacacionar para poder calcular el precio final:

-en Invierno: Bariloche tiene un aumento del 20% Cataratas y Cordoba tiene un
descuento del 10% Mar del Plata tiene un descuento del 20%

-en Verano: Bariloche tiene un descuento del 20% Cataratas y Cordoba tiene
un aumento del 10% Mar del Plata tiene un aumento del 20%

-en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un
aumento del 10% Mar del Plata tiene un aumento del 10% y Cordoba tiene el
precio sin descuento.

Validar el ingreso de datos"""

estadia_base = 15000
pregunta = "si"
while pregunta != 'no':

    estacion_del_ano = input('Ingrese la estacion del año deseada (Invierno/Verano/Otoño/Primavera): ')
    estacion_del_ano = estacion_del_ano.capitalize()
    while estacion_del_ano != 'Invierno' and estacion_del_ano != 'Verano' and estacion_del_ano != 'Otoño' and estacion_del_ano != 'Primavera':
        estacion_del_ano = input('ERROR. Ingrese la estacion del año deseada (Invierno/Verano/Otoño/Primavera): ')
        estacion_del_ano = estacion_del_ano.capitalize()

    localidad = input('Ingrese la localidad deseada (Bariloche/Cataratas/Mar del Plata/Cordoba) ')
    localidad = localidad.upper()
    while localidad != 'BARILOCHE' and localidad != 'CATARATAS' and localidad != 'MAR DEL PLATA' and localidad != 'CORDOBA':
        localidad = input('ERROR. Ingrese la estacion del año deseada (Invierno/Verano/Otoño/Primavera): ')
        localidad = localidad.upper()

    if estacion_del_ano == "Invierno":
        if localidad == "BARILOCHE":        
            precio_final = estadia_base - (estadia_base * 0.2)
        elif localidad == "CATARATAS" or localidad == "CORDOBA":
            precio_final = estadia_base - (estadia_base * 0.1)
        else:
            precio_final = estadia_base - (estadia_base * 0.2)
    elif estacion_del_ano == 'Verano':    
        if localidad == "BARILOCHE":        
            precio_final = estadia_base + (estadia_base * 0.1)
        elif localidad == "CATARATAS" or localidad == "CORDOBA":
            precio_final = estadia_base + (estadia_base * 0.1)
        else:
            precio_final = estadia_base + (estadia_base * 0.2)
    else:
        
        if localidad == "BARILOCHE":        
            precio_final = estadia_base + (estadia_base * 0.2)
        elif localidad == "CATARATAS" or localidad == "MAR DEL PLATA":
            precio_final = estadia_base - (estadia_base * 0.1)
        else:
            precio_final = estadia_base
    print(f'estacion del año elegida: {estacion_del_ano}\nLocalidad: {localidad}\n el precio total de la estadia es: {precio_final}')
    pregunta = input('Desea seguir preguntando [si/no]: ')


