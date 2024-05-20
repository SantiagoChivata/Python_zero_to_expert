######### Sentencia if / else #####################
""" 
NOTA: si un valor esta vacio automaticamente es false 
      y si la variable tiene cualquier valor automaticamente es true
      SE DEBE TENER MUCHO CUIDADO CON ESTO
"""

condition = 10

if condition:
    print('True condition')
else:
    print('False condition')
print('\n')

### para asegurarnos de que se esten cumpliendo correctamente las sentencias podemos agregar un '==' a la condicion
condition = False

if condition == True:
    print('True condition')
elif condition == False:
    print('False condition')
else:
    print('Diferent condition ')