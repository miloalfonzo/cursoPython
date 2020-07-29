
vector = [1, 2, 3]
vector2 = [-1, 0, 2]
vectorazo = []

for i in range(3):
    elemento = vector[i] * vector2[i]
    vectorazo.append(elemento)

print(vectorazo)

print(sum(vectorazo))
