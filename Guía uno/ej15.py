creditos = {
    "Matemáticas": 6,
    "Física": 4,
    "Química": 5
}

creditosT = 0

for materia, nota in creditos.items():
    print(f"La nota de {materia} es {nota}")
    creditosT = creditosT + nota

print(f"El total de créditos es de{creditosT}")
