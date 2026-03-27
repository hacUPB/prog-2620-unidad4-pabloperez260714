componentes = ["alas", "fuselaje", "motores", "tren de aterrizaje"]
print(componentes[0:4])  ## no encluye el 2, solo va desde el el primer dato hasta el cuarto dato  (0 y 3)


## listas vacias 
lista = []

### llenar la lista con 10 datos iguales 
for i in range(10):
    lista.append("hola")  ## recordar que el append es el que agrega datos a la lista

print (lista)

##llenar la lista con 3 datos agregados por el teclado
lista1 = []
for i in range(3):
    dato = input("ingrese el dato")
    lista1.append(dato)
print(lista1)
