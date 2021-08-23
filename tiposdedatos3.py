#diccionarios

palabras_ingles = {"hello": "hola", "day": "dia", "veinte": 20}

print(palabras_ingles)
print(palabras_ingles["day"])

palabras_ingles["hello"] = "salut"
print(palabras_ingles)
print(palabras_ingles["hello"])

palabras_ingles["night"] = "noche"
print(palabras_ingles)

del(palabras_ingles["night"])
print(palabras_ingles)

print(palabras_ingles["veinte"] + 1)

for palabra in palabras_ingles:
    print(palabra)

for clave in palabras_ingles:
    print(f"{clave} : {palabras_ingles[clave]}")

for clave, valor in palabras_ingles.items():
    print(clave, valor)

producto = {
    "id": 2,
    "nombre": "Heladera",
    "precio": 2000,
    "stock": 20
}
#javascript object notation