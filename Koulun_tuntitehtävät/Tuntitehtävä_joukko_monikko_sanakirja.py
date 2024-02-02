lista = ["john", 1, 5, 3, 1, "john", True, "john"]
newlista = []

for item in lista:
    if item not in newlista:
        newlista.append(item)


print(newlista)


lista11 = [1, 2, 3, 5]
lista22 = [4, [6, 8], 9]
lista33 = []
lista33.append(lista11 + lista22)
lista11.extend(lista22)

print(lista11)
print(lista33)
print(lista11[5][1])

#___

pelit = {"Monopoli", "Shakki", "Cluedo",}
print(pelit)

pelit.add("Dominion")
print(pelit)

pelit.remove("Shakki")
print(pelit)

pelit.add("Monopoli")
print(pelit)


print(list(set(lista)))


