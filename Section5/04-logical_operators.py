######### Operadores Logicos #####################

## Operador logico AND: Devuelve True si ambos operandos son True (a and b)
a = True
b = True

resultado = a and b
print(resultado)
#-- si alguno de los valores es False y se evalua con and retornara un False
a = True
b = False

resultado = a and b
print(resultado)
#-- si todos los valores son False y se evalua con and retornara un False
a = False
b = False

resultado = a and b
print(resultado)
print('\n')

## Operador logico OR: Devuelve True si alguno de los operandos es True (a or b)
a = True
b = True

resultado = a or b
print(resultado)

#-- si alguno de los valores es True y se evalua con or retornara un True
a = True
b = False

resultado = a or b
print(resultado)

#-- si todos los valores son False y se evalua con or retornara un False
a = False
b = False

resultado = a or b
print(resultado)
print('\n')

## Operador logico NOT: Invierte el valor de la variable (not a)
#-- si el valor de la variable es True y se evalua con not devolvera un False
a = True

resultado = not a
print(resultado)

#-- si el valor de la variable es False y se evalua con not devolvera un True
a = False

resultado = not a
print(resultado)
print('\n')

#*** EJERCICIO AND - Determinar si un numero se encuentra dentro de un rango de numeros ***#
print("EJERCICIO AND - Determinar si un numero se encuentra dentro de un rango de numeros")
valor = int(input('Escribe un numero: '))
minimo = 0
maximo = 5

dentroRango = valor >= minimo and valor <= maximo
print(dentroRango)

if dentroRango:
    print(f'El numero {valor} se encuentra dentro del rango {minimo} y {maximo}')
else:
    print(f'El numero {valor} no se encuentra dentro del rango {minimo} y {maximo}')

print('\n')


#*** EJERCICIO OR - Determinar si un padre puede asistir al juego de su hijo, solo puede asistir si esta en vacaciones o es un dia de descanso ***#
print("EJERCICIO OR - Determinar si un padre puede asistir al juego de su hijo, solo puede asistir si esta en vacaciones o es un dia de descanso")
vacaciones = False
diaDescanso = True

if  vacaciones or diaDescanso:
    print('Puede asistir al juego =)')
else:
    print('No puede asistir al juego =(')
print('\n')


#*** EJERCICIO NOT - Determinar si un padre puede o no asistir al juego de su hijo, si no tiene vacaciones ni dia de descanso no podra asistir ***#
print("EJERCICIO NOT - Determinar si un padre puede o no asistir al juego de su hijo, si no tiene vacaciones ni dia de descanso no podra asistir")
vacaciones = False
diaDescanso = False

if  not (vacaciones or diaDescanso):
    print('No puede asistir al juego =(')
else:
    print('Puede asistir al juego =)')

print('\n')


#*** EJERCICIO AND y OR - Determinar si una persona tiene entre los 20's ó los 30's ***#
print("EJERCICIO AND y OR - Determinar si una persona tiene entre los 20's ó los 30's")
edad = int(input('Escribe tu edad: '))

veintes = edad >= 20 and edad < 30
treitas = edad >= 30 and edad < 40

if veintes or treitas:
    if veintes:
        print(f'La persona tiene {edad} años, se encuentra dentro de los (20\'s)')
    elif treitas:
        print(f'La persona tiene {edad} años, se encuentra dentro de los (30\'s)')
    else:
        print('Fuera de rango')
else:
    print(f"La persona tiene {edad} años, no se encuentra dentro del rango de los 20's ni los 30's")

print('\n')

## Forma simplificada del operador AND, 
## la variable se cambia a la mitad de la expresion y se invierte el simblo > antes de la variable, el otro se deja como estaba
### Expresion sin simplificar:
## veintes = edad >= 20 and edad < 30
## treitas = edad >= 30 and edad < 40

edad = int(input('Escribe tu edad: '))


if 20 <=  edad < 30 or  30 <= edad < 40:
        print(f'La persona tiene {edad} años, se encuentra dentro de los (20\'s) ó (30\'s)')
else:
    print(f"La persona tiene {edad} años, no se encuentra dentro del rango de los 20's ni los 30's")

print('\n')


#*** EJERCICIO - Determinar cual de los numeros que ingresa el usuario es mayor ***#
print("EJERCICIO - Determinar cual de los numeros que ingresa el usuario es mayor")
num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))

if num1 > num2:
    print(f'el numero mayor es: {num1}')
else:
    print(f'El numero mayor es: {num2}')

print('\n')


#*** EJERCICIO - Tienda de libros
print("EJERCICIO - Tienda de libros")
print('Ingresa la informacion del libro:')
titulo = input('Ingresa el titulo del libro: ')
id = int(input('Ingresa el Id del libro: '))
precio = float(input('Ingresa el precio del libro: '))
envio = input('Indica si el envio es gratis (True/Flase): ')

if envio == 'True':
    envio = True
elif envio == 'False':
    envio = False
else:
    envio = 'Valor incorrecto'

print(f'''
Titulo: {titulo}
ID: {id}
Precio: {precio}
Envio gratuito: {envio}
''')