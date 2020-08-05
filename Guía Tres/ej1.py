# Crear una función que, a partir de un dato de entrada que sea en horas,
# nos informe cuántos minutos y cuántos segundos serían esas horas.
# Imprimir por pantalla dichos valores.

def minuseconds(hours):
    minutes = hours * 60
    seconds = hours * 3600
    print(f"La cantidad {hours} de horas serían {minutes} minutos y {seconds} segundos")

minuseconds(3)
