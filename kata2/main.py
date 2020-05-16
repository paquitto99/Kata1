'''
Escribir un programa que almacene la cadena de caracteres contraseña en una variable
pregunte al usuario por la contraseña e imprima por la pantalla si la contraseña introducida
por el usuario coincide con la guardada en la variable sin tener en cuenta mayusculas y minusculas
'''

password  = "contraseña" #la constante

password_input = input("Introduzca su password: ")  #se introduce la password

if password == password_input:
    print ("Su contraseña es correcta")
else:
    print ("Su contraseña no es correcta")