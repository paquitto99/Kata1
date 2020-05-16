'''
Una panaderia vende barras de pan a 3.40€ cada una. El pan que no es del dia tiene un descuento 
del 60%.

Escribe un programa que comience leyendo el número de barras vendidas que no son del dia.
Despues tu programa debe mostrar el precio habitual de una barra de pan, el descuento que se le 
hace por no ser fresca y el coste final total.

'''

precio = 3.49                #asignamos el precio a una variable, facilmente se puede cambiar
descuento = 0.6              # asignamos el descuento a una variable, facilmente se puede cambiar
cantidad_descontada = precio * descuento # calculamos la cantidad que se descuenta
precio_con_descuento = precio - cantidad_descontada # encontramos el precio rebajado tras el descuento

numero_de_barras = input("Introduce el número de barras vendidas: ") #introducimos el número de barras compradas

print ("Precio habitual: "+str(precio))
print ("Descuento: "+str(precio_con_descuento))
print ("Coste final: "+str(precio_con_descuento*int(numero_de_barras)))
