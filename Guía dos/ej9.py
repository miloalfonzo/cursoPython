amount = 2500
limit = float(
    input('Ingrese el limite disponible en su tarjeta de credito: $'))


if (limit > amount):
    print(f'Su saldo es de: {limit - amount }')
else:
    print(f'Le faltan {amount - limit } para realizar la compra')
