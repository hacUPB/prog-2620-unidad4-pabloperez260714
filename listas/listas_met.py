from random import randint
lista=[]
for i in range(100):
    dato = randint(0,9)
    lista.append(dato)
print(lista)
ocho = lista.count(8)
print(f"el numero ocho se repite {ocho} veces")

## ejercisio de carros
from random import randint
meses = ["enero","feberero","marzo","abril","mayo","junio","julio","agosto","semptiembre","octubre","noviembre","diciembre"]

lista=[]
for i in range(12):
    dato = randint(20,80)
    lista.append(dato)
print(lista)

mayor = max(lista)
mes = lista.index(mayor)  ## el index me muestra el indice del numero mayor 
print(f"se vendieron mas autos en {meses[mes]}")
print(f"se vendieron [mayor]")


