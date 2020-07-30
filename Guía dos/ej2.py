numbers = [40, 5, 100, 304, 55, 25, 87, 99, 63, 22]
numbers.sort()
numbMay = numbers[-1]
numbMen = numbers[0]
print(f"El mayor es {numbMay} y el menor es {numbMen}")
numbMayC = []
for numb in numbers:

    if numb > 100:
        numbMayC.append(numb)
if len(numbMayC) >= 3:
    for number in numbMayC:
        print(number)
else:
    for number in numbers:
        if number < 50:
            print(number)
