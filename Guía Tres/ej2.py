# Crear una función que devuelva una lista 
# con todos los números pares del 0 al 100 inclusive. 
# Imprimir esa lista por pantalla.

def even():
    hundredeven = []
    for i in range(101):
        if (i % 2 == 0):
            hundredeven.append(i)
    return hundredeven

print(even())