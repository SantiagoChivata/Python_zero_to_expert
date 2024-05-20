################ Convertir un numero a texto ##########################

number = int(input('Ingresa un numero entre 1 y 3: '))
numberText = ''

if number == 1:
    numberText = 'One'
elif number == 2:
    numberText = 'Two'
elif number == 3:
    numberText = 'Three'
else:
    numberText = 'number out of range'

print(f'Number entered: {number}, number in text: {numberText}')