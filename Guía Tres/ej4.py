#  Crear una función que, a partir de 4 números,
#  devuelva el mayor producto de dos de ellos. 
# Imprimir resultado por pantalla.

def prod():
    numbers = []
    for number in range(4):
        number = int(input("Ingresá un número: "))
        numbers.append(number)
    numbers.sort()
    for num in numbers:
        if num == 0: 
            numbers.pop(num)
            may = numbers[-2] * numbers[-1]
        else: 
            may = numbers [-2] * numbers[-1]
    print(may)

prod()
