aeronaves = {} 
def registrar_aeronave():
    print("\n REGISTRO DE AERONAVE")
    
    matricula = input("Matrícula: ")
    modelo = input("Modelo: ")
    horas_vuelo = float(input("Horas de vuelo: "))
    componentes = [] 
    num_componentes = int(input("Número de componentes: "))
    
    for i in range(num_componentes):
        print(f"\n Componente #{i+1}")
        
        nombre = input("Nombre: ")
        horas_uso = float(input("Horas de uso: "))
        limite = float(input("Límite de horas: "))
        datos_originales = (nombre, horas_uso, limite)
        componente = {
            "nombre": nombre,
            "horas_uso": horas_uso,
            "limite": limite,
            "datos": datos_originales
        }
        
        componentes.append(componente)
    
    aeronaves[matricula] = {
        "modelo": modelo,
        "horas_vuelo": horas_vuelo,
        "componentes": componentes
    }
    print("Aeronave registrada correctamente")
def mostrar_aeronaves():
    print("\n LISTA DE AERONAVES")
    if len(aeronaves) == 0:
        print("No hay aeronaves registradas.")
    else:
        for matricula, datos in aeronaves.items():
            print(f"\n {matricula} - {datos['modelo']}")
            print(f"Horas de vuelo: {datos['horas_vuelo']}")
            
            for comp in datos["componentes"]:
                print(f"  {comp['nombre']} -> {comp['horas_uso']} / {comp['limite']}")


def reporte_mantenimiento():
    print("\n REPORTE DE MANTENIMIENTO")
    reporte = []
    for matricula, datos in aeronaves.items():
        for comp in datos["componentes"]:
            if comp["horas_uso"] > comp["limite"]:
                
                alerta = (
                    matricula,
                    datos["modelo"],
                    comp["nombre"],
                    comp["horas_uso"],
                    comp["limite"]
                )
                
                reporte.append(alerta)
    
    if len(reporte) == 0:
        print("No hay componentes que requieran mantenimiento.")
    else:
        for alerta in reporte:
            print("\n MANTENIMIENTO REQUERIDO")
            print(f"Aeronave: {alerta[0]} ({alerta[1]})")
            print(f"Componente: {alerta[2]}")
            print(f"Horas: {alerta[3]} / Límite: {alerta[4]}")
while True:
    print("\n===============================")
    print(" SISTEMA AERONÁUTICO")
    print("1. Registrar aeronave")
    print("2. Mostrar aeronaves")
    print("3. Reporte de mantenimiento")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        registrar_aeronave()
    elif opcion == "2":
        mostrar_aeronaves()
    elif opcion == "3":
        reporte_mantenimiento()
    elif opcion == "4":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida")