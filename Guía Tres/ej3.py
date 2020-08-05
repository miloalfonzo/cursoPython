#Crear una función que, a partir de un mensaje,
#  nos devuelva una lista con todos los números,
#  si los hay, que aparecen en dicho mensaje.

def msg(msg):
    numbers = []
    for number in msg:
        if number.isdigit():
            numbers.append(number)
    print(numbers)

msg("Tengo 21 años")