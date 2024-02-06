"""
Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä
syöttää tyhjän merkkijonon. Kunkin nimen syöttämisen jälkeen ohjelma tulostaa
joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi
ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan
allekkain mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.
"""

nimi = input("Syötä nimi: \n")
nimet = set()


while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty")
    else:
        print("Uusi nimi")
        nimet.add(nimi)
    nimi = input("Syötä uusi nimi: \n")

for name in nimet:
    print(name)
