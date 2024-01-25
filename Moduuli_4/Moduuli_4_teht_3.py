#kysyy lukuja siihen saakka kunnes käyttäjä syöttää tyhjän merkkijonon.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

luku = input("Anna luku: \n")
pienin_luku = int(luku)
suurin_luku = int(luku)


while luku != "":
    luku = int(luku)
    if pienin_luku > luku:
        pienin_luku = luku
    if suurin_luku < luku:
        suurin_luku = luku
    luku = input("Anna luku: \n")

print(f"Pienin luku: {pienin_luku} ja suurin luku: {suurin_luku}.")
