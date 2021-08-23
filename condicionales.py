nombre = "Pia"
edad = 15
persona_masculina = True
persona_feminina = True

if nombre == "Gaston":
    print("Es cierto la variable nombre es Gaston")
elif nombre == "Mario":
    print("Tu nombre es Mario")
elif nombre == "Belen":
    print("Tu nombre es igual a Belen")
else:
    print("Tu nombre no es Gaston, ni Mario, ni Belen")
    if nombre == "Mia":
        print("Tu nombre es Mia")

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#and y 
if persona_masculina == True and persona_feminina == False:
    #print("Una de las dos condiciones se cumple") esto va con or
    print("Se cumplen las dos condiciones")
else:
    print("No se cumplen las condiciones")

if not persona_masculina:
    print("Persona masculina")