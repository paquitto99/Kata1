'''
Escribir un programa que al usuario un número entero y muestre arbol de asteriscos.
'''

n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
   print("*"*(i+1))