calif = {
    "Jesse": 2,
    "Walter": 10,
    "Gale": 9,
    "Skinny Pete": 7,
    "Hank": 8
}

for name, cal in calif.items():
    if cal >= 7:
        print(f"{name}: {cal}")
