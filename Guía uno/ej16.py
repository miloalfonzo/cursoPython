datoPersona = {}
yes = 'si'

while yes == 'si':
    tipo = input("¿Qué dato vas a introducir? ")
    dato = input(f"{tipo} : ")
    datoPersona[tipo] = dato
    print(datoPersona)
    yes = input(
        "¿Quieres introducir más información? Escriba si en caso afirmativo y no en caso negativo ").lower()
