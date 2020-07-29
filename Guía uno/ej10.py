abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r",
       "s", "t", "u", "v", "w", "x", "y", "z"]
abc2 = abc.copy()


for i in abc2:
    vocales = ["a", "e", "i", "o", "u"]
    for voc in vocales:
        if i == voc:
            abc2.remove(i)

print(abc2)
