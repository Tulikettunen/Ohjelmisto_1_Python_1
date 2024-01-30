ihmiset = ["Fiona", "Debby", "Carl", "Ian", "Lip","Liam"]

print(ihmiset[0]) #indexi 0, listan ensimmäinen arvo
print(ihmiset[1:3]) #i
print(ihmiset[1:])
print(ihmiset[:5])
print(ihmiset[::-1]) #kääntää listan ympäri

x = "Ian" in ihmiset #tarkistaa onko joku asia listassa vai ei, palauttaa totuusarvon
print(x)

items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
parittomat = []

for i in items:
    if i % 2 == 1:
        parittomat.append(i)

print(parittomat)

prob = [0.52, 0.49, 0.72, 0.81, 0.12, 0.11]
probnew = []

for i in prob:
    if i >= 0.5:
        probnew.append(1)
    else:
        probnew.append(0)
print(probnew)

ihmiset.append("Jimmy")
print(ihmiset)

ihmiset.extend(["Frank", "Sammy"])
print(ihmiset)

ihmiset.pop(7)
print(ihmiset)


print(list(range(0, 100, 11)[1:]))

for luku in range(6):
    print("Moi!")

print(list(range(90,4,-5)))

