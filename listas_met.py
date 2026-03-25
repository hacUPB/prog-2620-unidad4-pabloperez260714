from random import randint

lista=[]
for i in range(100):
    dato = randint(0,9)
    lista.append(dato)
print(lista)
ocho = lista.count(8)
print(f"el numero ocho se repite {ocho} veces")