######### Ciclo While in Python #####################
"""
Un ciclo while en Python es una estructura de control que repite un bloque de código 
mientras una condición especificada sea verdadera. Se evalúa la condición antes de cada iteración
y si es verdadera, el bloque de código se ejecuta; si es falsa, el ciclo termina.
"""

contador = 0

while contador < 3:
    print(contador)
    contador += 1 #En esta linea se aumenta el valor de la variable una vez (+1)
else:
    print('final del ciclo while')