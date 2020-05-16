'''
Crear un programa que te devuelva la tabla de multiplicar de un número que le pasamos.
'''

n = int(input("Introduce el número de la tabla que deseas.:"))

for i in range(10):
   print(str(n) + " x " + str(i+1) + " = " + str((i+1)*n))