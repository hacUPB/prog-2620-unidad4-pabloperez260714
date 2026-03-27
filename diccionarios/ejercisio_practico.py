vuelo = {

    "aerolínea": "Avianca",

    "vuelo": "AV123",

    "origen": "BOG",

    "destino": "MDE"

}
# Acceso a los Valores
ciudad_llegada = vuelo["destino"]
print (ciudad_llegada)
# Modificación de un valor existente
vuelo["destino"] = "CLO"
print(vuelo["destino"])
# Agregar un nuevo par clave-valor
vuelo["estado"] = "En el aire"
print (vuelo["estado"])
# Uso del método ".get"
piloto = vuelo.get("piloto", "No existe")  
print (piloto)
# Eliminar un dato
del vuelo["vuelo"]
print (vuelo)