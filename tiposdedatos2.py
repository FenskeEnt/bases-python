
nombres = ["Gaston", "Belen", "Mia", "Pia"]
edades = [20, 21, 25, 35, 64, 14, 12]
numeros = [18, 19]
apellidos = [
    ["Fenske", "Benitez"], 
    ["Lopez, Rodriguez"], 
    ["Gonzales", "Vilches"]
]

print(nombres)
nombres.append("Ramon")
print(nombres)
nombres.pop()
print(nombres)
cantidad_elementos = len(nombres)
print(cantidad_elementos)
print(nombres[0])

print(apellidos)
print(apellidos[0])
print(apellidos[0][1])

print(max(edades))
print(min(edades))
print(sorted(edades))

edades.remove(64)
print(edades)

#edades.reverse()

edades.extend(nombres)
print(edades)

for nombre in nombres:
    print(nombre)

pares = []
for i in range(100):
    if i % 2 == 0:
        pares.append(i)
print(pares)

pares = [i for i in range(100) if i % 2 == 0]
print(pares)

