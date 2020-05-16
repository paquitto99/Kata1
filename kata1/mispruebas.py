a = 20
b = "texto"
c = True

def miPrimeraFuncion(variable):
    print ("si las tabulaciones no están bien formateadas, directamente rompen la funcion en este caso")
    return 2+2+variable
n = int(input("Introduce el valor: "))
r = miPrimeraFuncion(n)

print (r)

if r == 9:
    print ("llamaste a la primera funcion con el valor 5")
else:
    print ("No sé que valor le diste a la función, pero no fué 5")

for i in (1,2,3,4):
    print (i)