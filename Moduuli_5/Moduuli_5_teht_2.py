"""
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä
syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista
luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille
argumentiksi reverse=True.
"""


number = input("Give a number: ")
lista = []

while number != "":
    try:
        number = int(number)
        lista.append(number)
        number = input("Give a number: ")
    except:
        number = input("Give a valid number: ")


lista.sort(reverse=True)
print(lista[0:5])

