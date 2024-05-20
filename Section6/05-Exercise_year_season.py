################ Ejercicio: estacion del año segun el mes ##########################
## El usuario debe ingresar un numero del 1 al 12 y de acuerdo a ese numero se indicara en que estacion del año esta.

mes = int(input('Ingresa un numero entre 1 y 12: '))
estacion = None

if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otoño'
else:
    estacion = 'No ingresaste un mes valido'
    
print(f'Para el mes {mes} la estacion del año es: {estacion}')