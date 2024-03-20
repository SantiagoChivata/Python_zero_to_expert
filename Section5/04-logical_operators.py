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