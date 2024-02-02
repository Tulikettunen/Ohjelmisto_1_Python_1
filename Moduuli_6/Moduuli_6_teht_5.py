"""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina
saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja
tulostat sen jälkeen sekä alkuperäisen että karsitun listan.
"""


lista = [1, 4, 3, 7, 44, 64, 77, 98, 13, 3, 2, 0, 65, 4, 16, 7]
newlista = []

def parilliset(lista):
    for num in lista:
        if num % 2 == 0:
            newlista.append(num)
    return newlista


print(f" Alkuperäinen lista oli: {lista}.")
print(f"Uusi vain parilliset numerot sisältävä lista on: {parilliset(lista)}")
