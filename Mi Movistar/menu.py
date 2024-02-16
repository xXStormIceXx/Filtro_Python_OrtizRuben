import MovistarCRUD as file

contador = 0 
categoria = {}
while (contador != 6):
    print(" ==================================", "\n", "*   BIENVENIDO ADMINISTRADOR   *", "\n","==================================")
    print("1. Usuarios","\n", "2. Productos y Servicios", "\n", "3. Promosiones", "\n", "4. Informes/Reportes", "\n", "0. salir")
    respuesta = int(input("Selecciones una opcion (0-5): "))
    file.limpiar_pantalla
    if (respuesta == 1):
        print(" ============================", "\n", "*      USUARIOS      *", "\n","==================================")
        print("1. Crear Nuevo Usuario","\n", "2. Asignar Categoria Usuario","\n","0. Menu de Inicio")
        ingreso = int(input("Selecciona una Opcion (0-2)"))
        if (ingreso == 1):
            file.crear_usuario()
            file.limpiar_pantalla
        if (ingreso == 2):
            file.actualizar_tipo_Usuario()
            file.limpiar_pantalla
        if (ingreso == 0):
            input("")
    file.limpiar_pantalla
    if (respuesta == 2):
        print("=============================", "\n", "* PRODUCTOS Y SERVICIOS *", "\n","==================================")
        print("1. Fibra Optica","\n", "2. Planes Pospago", "\n", "3. Planes Prepago", "\n", "4. Telefonia Hogar + TV Full", "\n", "5. Telefonia, TV Full", "\n", "0. Menu de Inicio")
    file.limpiar_pantalla
    if (respuesta == 3):
        print("=============================", "\n", "*    PROMOCIONES    *", "\n","==================================")
        print("1. Combo Personal","\n", "2. Combo Familiar","\n","0. Menu de Inicio")
    file.limpiar_pantalla
    if (respuesta == 4):           
        print("=============================", "\n", "*  INFORMES/REPORTES  *", "\n","==================================")
        print("1. Lista Productos y Servicios","\n", "2. Productos y Servicios mas Usados", "\n", "3. Lista de Productos y Servicios Por Ususario","\n","0. Menu de Inicio")
    if (respuesta == 0):
        break