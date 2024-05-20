################ Ejercicio: Etapas de la vida segun tu edad ##########################
## El usuario debe ingresar la edad que tiene y cn base en es se indicara en que etapa de la vida esta.

edad = int(input('Ingresa tu edad: '))

if 0 <= edad  <= 10:
    etapa = 'La infancia es increible!'
elif 10 < edad  <= 20:
    etapa = 'Muchos cambios y mucho estudio!'
elif 20 < edad <= 30:
    etapa = 'Amor y comienza el trabajo'
elif 30 < edad  <= 60:
    etapa = 'Disfrutar la vida, aprovecha cada instante!'
else:
    etapa = 'Agradecer por lo vivido O:)'
    
print(f'tu edad es: {edad} años, esta en la etapa de: {etapa}')
