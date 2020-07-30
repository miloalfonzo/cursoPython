message = (input('Ingrese su mensaje: '))
reverse = message

if (len(message) > 100):
    print(message)
elif (len(message) >= 50 and len(message) <= 100):
    print(reverse)
else:
    print('su mensaje es demasiado corto')
