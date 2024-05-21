myVariable = "Este es mi saludo desde python"
print(myVariable)
#######################Seccion 3 del curso - Variables ###########################
x=10
y=2
z = x +y
print(id(x))
print(z)

nombre= "Santi el mejor"
telefono = 3219750008
email = "sac.94@hotmail.com"

print (nombre, telefono, email)

######### Saltos de Linea ##########
print('\n')
print('\n')
print('\n')
####################### Seccion 4 del curso - Tipos de Datos #############################

print("####Seccion 4 del curso - Tipos de Datos #####")

x = 10 # tipo Entero
print(x)
print(type(x)) ## imprimir tipo de variable
print('\n')

x = "Santi eres the best" # tipo String
print(x)
print(type(x))
print('\n')

x = True ## tipo Boolean
print(x)
print(type(x))
print('\n')

x = 10.4 # tipo float
print(x)
print(type(x))
print('\n')

miGrupoFavorito = "CHD"
enunciado = "mi grupo favorito es: "
print( enunciado + miGrupoFavorito)  ## tipo Cadena
print('\n')

##convertir tipo de datos
num1 = "1"
num2 = "2"
print("Suma de variables string convertidas a int")
print("suma: ", int(num1) + int(num2))
print('\n')

## Procesar entrada del usuario con la funcion input
mensaje = input("Escribe un mensaje: ")
print("El mensaje ingresado es: " + mensaje)
print('\n')

## Convertir tipo de datos junto con la funcion input ya que por defecto la funcion input devuelve un str
numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)

print('\n')

## Ejercicio - Califica tu dia

enunciado = int(input("Califica del 1 al 10 como estuvo tu dia: "))
print("Tu dia estuvo de: ", enunciado)
print('\n')

## Ejercicio - Informacion de un libro
libro = input("Ingresa el titulo del libro: ")
autor = input("Ingresa el nomnre del autor del libro: ")
print(libro ,"fue escrito por", autor)

