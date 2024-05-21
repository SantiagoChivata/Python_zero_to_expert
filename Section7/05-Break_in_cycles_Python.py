######### Instruccion break in Python #####################
"""
La instrucción break en Python se utiliza dentro de ciclos (for o while) para terminar la ejecución
del ciclo de manera anticipada.
Cuando se ejecuta break, el control del programa sale inmediatamente del ciclo,
y la ejecución continúa con la siguiente instrucción después del ciclo.
"""
##** imprimimos la bocal 'a' cada vez que la encuentre en la cadena 'Holanda'
for letra in 'Holanda':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
else:
    print('Fin ciclo for\n')

##** Detendremos el ciclo con la Instruccion break cuando encuentre la primer bocal 'a' en la cadena 'Holanda'
for letra in 'Holanda':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break
else:
    print('Fin ciclo for\n')
