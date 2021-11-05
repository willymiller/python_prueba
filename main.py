a = 20
b = 50

def sumar(a,b):
    """función que devuelve la suma de los parámetros a y b"""
    suma = a + b
    return suma

total = sumar(a,b)
print(total)

super_lista = [0,1,2,3,4,5,6]

print(6 in super_lista)
print(10 in super_lista)

cont = 1
suma = 0

while cont <= 5:
    num = int(input("Ingrese un número: "))
    suma = suma + num
    cont = cont + 1

print("la suma total es: " + str(suma))
