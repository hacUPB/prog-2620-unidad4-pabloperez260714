aeronaves = {}
def registrar_aeronave():
    print("\nREGISTRO DE AERONAVE")
    
    matricula = input("Matrícula: ")
    modelo = input("Modelo: ")
    horas = float(input("Horas de vuelo: "))
    
    lista_componentes = []  
    cantidad = int(input("¿Cuántos componentes desea registrar?: "))
    for i in range(cantidad):
        print(f"\nComponente #{i+1}")
        nombre = input("Nombre: ")
        horas_uso = float(input("Horas de uso: "))
        limite = float(input("Límite de horas: "))
        datos = (horas_uso, limite)
        componente = {
            "nombre": nombre,
            "datos": datos
        }
        
        lista_componentes.append(componente)
    aeronaves[matricula] = {
        "modelo": modelo,
        "horas": horas,
        "componentes": lista_componentes
    }
    print("Aeronave guardada")
def mostrar_datos():
    print("\n DATOS DEL SISTEMA")
    if len(aeronaves) == 0:
        print("No hay aeronaves registradas.")
        return
    for matricula, datos in aeronaves.items():
        print(f"\n {matricula} - {datos['modelo']}")
        print(f"Horas de vuelo: {datos['horas']}")
        for comp in datos["componentes"]:
            horas_uso, limite = comp["datos"]  
            
            print(f" {comp['nombre']}")
            print(f" Horas: {horas_uso} / Límite: {limite}")
def reporte():
    print("\n REPORTE DE MANTENIMIENTO")
    hay_alertas = False
    for matricula, datos in aeronaves.items():
        for comp in datos["componentes"]:
            horas_uso, limite = comp["datos"]  # tupla
            if horas_uso > limite:
                hay_alertas = True
                
                print("\nMANTENIMIENTO REQUERIDO")
                print(f"Aeronave: {matricula} ({datos['modelo']})")
                print(f"Componente: {comp['nombre']}")
                print(f"Horas: {horas_uso} / Límite: {limite}")
    
    if not hay_alertas:
        print("Todo en buen estado")
while True:
    print("\n===============================")
    print("SISTEMA AERONÁUTICO")
    print("===============================")
    print("1. Registrar aeronave")
    print("2. Mostrar datos")
    print("3. Ver reporte")
    print("4. Salir")
    
    opcion = input("escoge una opció: ")
    
    if opcion == "1":
        registrar_aeronave()
    elif opcion == "2":
        mostrar_datos()
    elif opcion == "3":
        reporte()
    elif opcion == "4":
        print("Saliendo")
        break
    else:
        print("Opción inválida")