## import sirve para traer una biblioteca que no pertenece a python
import random
print(random.randint(2,10))

## Crear una lista con 100 numeros aleatorios entre 100 y 200
lista = []
for i in range (100):
    lista.append(random.randint(100,200))
print(lista)

mayor = max(lista)  ## muestra el numero mas grande
print(f" el numero mas grande de la lista es {mayor}")

## implemtar el max usando un bucle
indice = 0
may = lista[0]
while indice < 99:
    if may < lista[indice + 1]: 
        may = lista[indice + 1]
    indice = indice + 1
print(f"El mayor calculado a mano es: {may}")
 
