divisas = {
    'Euro': '€',
    'Dollar': '$',
    'Yen': '¥'
}
divisa = input('Ingresa una divisa: ')

if divisa in divisas:
    print(divisas[divisa])
else:
    print('La divisa no existe en nuestros datos')
