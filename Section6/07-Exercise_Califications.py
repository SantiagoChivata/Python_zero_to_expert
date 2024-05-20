################ Ejercicio: Calificaciones para un colegio ##########################
"""
El objetivo es crear un sistema de calificaciones con las siguientes indicaciones:

El usuario debe ingresar un valor entre 0 y 10.
Si esta entre 9 y 10 la calificacion sera una A
Si esta entre 8 y menor a 9 la calificacion sera una B
Si esta entre 7 y menor a 8 la calificacion sera una C
Si esta entre 6 y menor a 7 la calificacion sera una D
Si esta entre 0 y menor a 6 la calificacion sera una F

Cualquier otro valor debe imprimir: valor incorrecto

"""

calificacion = int(input('Ingrese la nota entre 0 y 10: '))

if  9 <=  calificacion <=  10:
    nota = 'A'
elif 8 <= calificacion < 9:
    nota = 'B'
elif 7 <= calificacion < 8:
    nota = 'C'
elif 6 <= calificacion < 7:
    nota = 'D'
elif 0 <= calificacion < 6:
    nota = 'F'
else:
    nota = 'Valor incorrecto'

print(f'Para la calificacion {calificacion} la nota correspondiente es: {nota}')