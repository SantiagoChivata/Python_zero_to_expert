######### Instruccion continue in Python #####################
"""
La instrucción continue en Python se utiliza dentro de ciclos (for o while)
para saltar a la siguiente iteración del ciclo, omitiendo el resto del código en la iteración actual.
"""
##** Imprimimos el indice en un rango de 6 numeros, es decir desde el indice 0 al indice 5
for i in range(6):
    print(f'Indice: {i}')
print('\n')

##** Imprimimos solo los numeros pares en un rango de numeros hasta el 6
for i in range(6):
    if i % 2 == 0:
        print(f'Numero par: {i}')
print('\n')

"""
INSTRUCCION CONTINUE:
Ahora utilizamos la instruccion continue, se verifica si el resultado de dividir un numero entre 2 
es diferente de cero, si es asi seria un numero impar, y lo saltaremos con la instruccion continue
""" 
print('INSTRUCCION CONTINUE:')
for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Numero par: {i}')