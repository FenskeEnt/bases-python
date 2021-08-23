
def saludar():
    print("Hola que tal")


def saludar_persona(persona="Persona generica"):
    print(f"Hola que tal {persona}")


saludar()
saludar_persona("Gaston")


def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def dividir(num1, num2):
    return num1 / num2

def multiplicar(num1, num2):
    return num1 * num2

#resultado = sumar(2, 2)
#print(resultado)
#print(sumar(3,3))

def programa():
    menu = int(input("""
[1]Para sumar
[2]Para restar
[3]Para divir
[4]Para multiplicar
[5]Para salir del programa
>>> """))
    if menu == 1:
        num1 = int(input("Ingrese el primer numero para sumar: "))
        num2 = int(input("Ingrese el primer numero para sumar: "))
        resultado = sumar(num1, num2)
        print(f"El resultado de la suma es = {resultado}")
    elif menu == 2:
        num1 = int(input("Ingrese el primer numero para restar: "))
        num2 = int(input("Ingrese el primer numero para restar: "))
        resultado = restar(num1, num2)
        print(f"El resultado de la resta es = {resultado}")
    elif menu == 3:
        num1 = int(input("Ingrese el primer numero para dividir: "))
        num2 = int(input("Ingrese el primer numero para dividir: "))
        resultado = dividir(num1, num2)
        print(f"El resultado de la division es = {resultado}")
    elif menu == 4:
        num1 = int(input("Ingrese el primer numero para multiplicar: "))
        num2 = int(input("Ingrese el primer numero para multiplicar: "))
        resultado = multiplicar(num1, num2)
        print(f"El resultado de la multiplicacion es = {resultado}")
    elif menu == 5:
        print("Saliendo del programa...")
        exit()
    else:
        print("Esa opcion no esta en el menu")

while True:
    programa()