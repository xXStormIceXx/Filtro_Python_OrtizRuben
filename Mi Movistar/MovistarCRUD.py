import json
import os

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def cargar_datos(ruta):
    try:
        fd = open(ruta, "r")
    except Exception as e:
        try:
            fd = open(ruta, "w")
        except Exception as d:
            print("Error al intentar abrir el archivo\n", d)
            input("Presione cualquier tecla para continuar\n")
            return None
    try:
        linea = fd.readline()
        if linea.strip() != "":
            fd.seek(0)
            lstPersonal = json.load(fd)
        else:
            lstPersonal = []
    except Exception as e:
        print("Error al cargar la información\n", e)
        input("Presione cualquier tecla para continuar\n")
        return None
        
    try:
        if not fd.closed:
            fd.close()
    except Exception as e:
        print("Error al cerrar el archivo.\n", e, "\n")
        input("Presione cualquier tecla para continuar\n")
        return None
    return lstPersonal

def cargar_datos(ruta):
    try:
        fd = open(ruta, "r")
    except Exception as e:
        try:
            fd = open(ruta, "w")
        except Exception as d:
            print("Error al intentar abrir el archivo\n", d)
            input("Presione cualquier tecla para continuar\n")
            return None
    try:
        linea = fd.readline()
        if linea.strip() != "":
            fd.seek(0)
            lstPersonal = json.load(fd)
        else:
            lstPersonal = []
    except Exception as e:
        print("Error al cargar la información\n", e)
        input("Presione cualquier tecla para continuar\n")
        return None
        
    try:
        if not fd.closed:
            fd.close()
    except Exception as e:
        print("Error al cerrar el archivo.\n", e, "\n")
        input("Presione cualquier tecla para continuar\n")
        return None
    return lstPersonal

def guardar_datos(lstPersonal, ruta):
    # Función que guarda los datos de la lista de personal
    # en un arcivo JSON
    # Devuelve True: si los datos fueron guardados correctamente
    # Devuelve False: si los datos no se pudieron guardar
    try:
        fd = open(ruta, "w")
    except Exception as e:
        print("Error al abrir el archivo para guardar al empleado.\n", e)
        input("Presione cualquier tecla para continuar\n")
        return False
    
    try:
        json.dump(lstPersonal, fd, indent=4)
    except Exception as e:
        print("Error al guardar la información del empleado.\n", e)
        input("Presione cualquier tecla para continuar\n")
        return False
    
    try:
        if not fd.closed:
            fd.close()
    except Exception as e:
        print("Error al cerrar el archivo.")
        input("Presione cualquier tecla para continuar\n")
        return False
    
    return True

def crear_usuario():
    identificacion = str(input("ingresa el numero de identificación: ")) #Al inicio debes indicar donde quieres ingresar la informacion en  el JSON
    nombre = str(input(" ingresa el nombre: "))
    apellido1 = str(input(" ingresa el primer apellido: "))
    apellido2 = str(input(" ingresa el segundo apellido: "))
    direccion = str(input(" ingresa la direccion del Usuario: "))
    telefono1 = str(input(" ingresa el telefono celular: "))
    telefono2 = str(input(" ingresa el telefono fijo: "))
    edad = str(input(" ingresa la edad: "))
    estado = str(input(" ingrese el tipo de cliente: "))
    pys = str(input(" ingresa los PyS contratados: "))
    data = cargar_datos("proyecto_python/data.json")
    id = len(data) + 1;
    nuevo_objeto = {"id": id, 
                    'identificacion':identificacion,
                    'nombre':nombre,
                    'apellido1':apellido1,
                    'apellido2':apellido2,
                    'direccion':direccion,
                    'telefono1':telefono1,
                    'telefono2':telefono2,
                    'edad':edad,
                    'estado':estado,
                    'PyS contratados': pys}
    data.append(nuevo_objeto)
    guardar_datos(data, 'proyecto_python/data.json')

def leer_camper():
    with open('datos.json', 'r') as archivo:
        data = json.load(archivo)
    if data:
        print("Lista de Campers:")
        for usuario in data:
            print(f"Identificacion:{usuario['identificacion']}, Nombre: {usuario['nombre']}, Apellido 1:{usuario['apellido1']}, Apellido2:{usuario['apellido2']}, Direccion:{usuario['direccion']}, Telefono1:{usuario['telefono1']}, Telefono2:{usuario['telefono2']}, Edad: {usuario['edad']}, Estado: {usuario['estado']}")
    else:
        print("No hay Usuarios para mostrar.")

def actualizar_tipo_Usuario(nombre, nueva_edad):
    try:
        with open('datos.json', 'r') as archivo:
            datos = json.load(archivo)
            for registro in datos:
                if registro['nombre'] == nombre:
                    registro['edad'] = nueva_edad

        with open('datos.json', 'w') as archivo:
            json.dump(datos, archivo, indent=2)
    except FileNotFoundError:
        print("No hay registros.")