'''
Crear un programa que te devuelva la tabla de multiplicar de un número que le pasamos.
'''
#castingData
while True:
    n = input("Introduce el número de la tabla que deseas.:")

    n = int(n)
    print(n)

    if (n in range(10)):
        break
    
 
for i in range(10):
    print(str(n) + " x " + str(i+1) + " = " + str((i+1)*n))

