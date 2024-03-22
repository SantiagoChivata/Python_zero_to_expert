########## Comparacion en python ##############
## El operador de igualdad se realiza con el simbolo = 2 veces seguidas '==', 
## si la comparacion no es igual el resultado es False, si es igual el resultado es True
a = 4
b = 2

resultado = a == b
print(f'Resultado == : {resultado}')

## El operador de diferencia se realiza con los simbolos '!='
## si no hay diferencia el resultado es False, si existe una diferencia el resultado es True
resultado = a != b
print(f'Resultado != : {resultado}')

## El operador de mayor que se realiza con el simbolo '>'
## si el valor es menor el resultado es False, si el valor es mayor el resultado es True
resultado = a > b
print(f'Resultado > : {resultado}')

## El operador de mayor ó igual se realiza con los simbolos '>='
## si el valor es menor el resultado es False, si el valor es mayor ó igual el resultado es True
resultado = a >= b
print(f'Resultado >= : {resultado}')

## El operador de menor que se realiza con el simbolo '<'
## si el valor es menor el resultado es True, si el valor es mayor el resultado es False
resultado = a < b
print(f'Resultado < : {resultado}')

## El operador de menor ó igual se realiza con los simbolos '<='
## si el valor es menor el resultado es True, si el valor es mayor ó igual el resultado es False
resultado = a <= b
print(f'Resultado <= : {resultado}')
print('\n')

#*** EJERCICIO - Determinar si un numero es par o impar ***#
num = int(input('Escriba un numero: '))

if num % 2 == 0:
    print(f'El numero {num} es par!')
else:
    print(f'El numero {num} es impar!')
print('\n')

#*** EJERCICIO - Determinar si una persona es mayor o menor de edad ***#
edad = int(input('Escriba su edad en numeros: '))

if edad >= 18:
    print('Eres Mayor de edad, tomate una cerveza!')
else:
    print('Eres Menor de edad, tomate un juguito (^=^)')