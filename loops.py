
tabla_a_calcular = int(input("Ingrese la tabla que desea calcular: "))
hasta_donde = int(input(f"Hasta que numero desea calcular la tabla del {tabla_a_calcular}: "))

"""
print(f"{tabla_a_calcular} x 1 = {tabla_a_calcular * 1}")
print(f"{tabla_a_calcular} x 2 = {tabla_a_calcular * 2}")
print(f"{tabla_a_calcular} x 3 = {tabla_a_calcular * 3}")
print(f"{tabla_a_calcular} x 4 = {tabla_a_calcular * 4}")
print(f"{tabla_a_calcular} x 5 = {tabla_a_calcular * 5}")"""

#num = 1
for i in range(hasta_donde):
    print(f"{tabla_a_calcular} x {i+1} = {tabla_a_calcular * (i+1)}")
    #num = num + 1

while 1 != 3:
    print("hola")