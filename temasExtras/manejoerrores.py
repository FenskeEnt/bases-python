


try:
    menu = int(input("Ingrese una opcion valida: "))
    print(f"Ha ingresado la opcion {menu}")
except ValueError as error:
    print(f"No puede ingresar ese tipo de dato, error: {error}")
