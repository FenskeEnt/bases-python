"""
Hacer un programa que le pida al usuario que ingrese su edad y su sexo,
si el usuario es mayor de edad y ademas es menor de 65 años le debe permitir
al usuario quedarse en el programa, en caso
contrario el programa debe deternese. Si es sexo es masculino que el programa
salude al usuario como un caballero y si el sexo es femino que el programa salude al
usuario como una dama
-Para que el usuario ingrese su sexo hacer un menu con condiciones.
"""
edad = int(input("Ingresa tu edad: "))
masculino = False
sexo = int(input("""
Ingrse su sexo:
[1]Para masculino
[2]Para femenino
>>> """))
if sexo == 1:
    masculino = True
elif sexo == 2:
    masculino = False
else:
    print("Esa opcion no es valida")
    exit()

if edad >= 18 and edad <= 65:
    if masculino:
        print(f"Hola caballero de {edad} años de edad")
    else:
        print(f"Hola dama de {edad} años de edad")
else:
    print("Lo siento para usar el programa debe ser mayor de 18 y menor de 65")
    exit()
    