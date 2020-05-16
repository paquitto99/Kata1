'''
Escribir un programa para una empresa que tiene salas de juegos para todas las 
edades y quiere calcular de forma automática el precio que debe cobrar asus
clientes por entrar. El programa debe preguntar al usuario la edad del cliente
y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede 
entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18
años 10€
'''

edad = int(input("Introduce tu edad: "))        # se pide la edad a la vez que se transforma en numero

if edad < 4:                        # comprobamos si es menor de 4 años
    print ("Puede entrar GRATIS")
else:                               # si no lo és pasamos a comprobar si es menor de 18 años
    if edad < 18:
        print ("Puede entrar pagando solo 5€")
    else:                           # si llega hasta aquí sabemos con seguridad que es mayor de 18 años
        print ("Para entrar debes pagar 10€")

