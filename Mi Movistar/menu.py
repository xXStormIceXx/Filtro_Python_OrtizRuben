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
    file.limpiar_pantalla
    if (respuesta == 2):
        print("=============================", "\n", "* PRODUCTOS Y SERVICIOS *", "\n","==================================")
    file.limpiar_pantalla
    if (respuesta == 3):
        print("=============================", "\n", "*    PROMOCIONES    *", "\n","==================================")
    file.limpiar_pantalla
    if (respuesta == 4):           
        print("=============================", "\n", "*  INFORMES/REPORTES  *", "\n","==================================")
    if (respuesta == 0):
        break