## Operador suma '+'
operandoA = 3
operandoB = 2
suma = operandoA + operandoB
print('El resultado de la suma es:',suma)
print(f'El resultado de la suma es: {suma}') ## otra manera de imprimir datos (Es la que mas se maneja)
print('\n')

## Operador resta '-'
operandoA = 3
operandoB = 2
resta = operandoA - operandoB
print(f'El resultado de la resta es: {resta}')
print('\n')

## Operador multiplicacion '*'
operandoA = 3
operandoB = 2
multiplicacion = operandoA * operandoB
print(f'El resultado de la multiplicacion es: {multiplicacion}')
print('\n')

## Operador division '/'
operandoA = 3
operandoB = 2
division = operandoA / operandoB
print(f'El resultado de la division es: {division}')
# si queremos que el resultado sea un numero entero y no un float en la operacion se asignan 2 /
division = operandoA // operandoB
print(f'El resultado de la division es: {division}')
print('\n')

## Operador modulo o restante '%'
operandoA = 3
operandoB = 2
modulo = operandoA % operandoB
print(f'Resultado del residuo de la división (módulo) es: {modulo}')
print('\n')

## Operador exponente '**'
operandoA = 3
operandoB = 2
exponente = operandoA ** operandoB
print(f'Resultado del exponente es: {exponente}')
print('\n')

#*** EJERCICIO - Rectangulo, se debe calcular el area y el perimetro de un Rectangulo ***#
alto = int(input('Ingresa el alto del rectangulo: '))
ancho = int(input('Ingresa el ancho del rectangulo: '))
area = alto * ancho
perimetro = (alto + ancho) * 2
print(f'Area del rectangulo: {area}')
print(f'perimetro del rectangulo: {perimetro}')
print('\n')