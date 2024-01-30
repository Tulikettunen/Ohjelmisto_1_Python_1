"""
Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten,
että jako menee tasan.
Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös
luvulla 3 tai luvulla 7.
"""


number = int(input("Enter a number: "))
e = 2

for i in range(2, round(number / 2)):
    if number % i == 0:
        print(f"Luku {number} ei ole alkuluku, se on jaollinen ainakin luvulla {i}")
        break
    e += 1

if e == round(number / 2):
    print(f"Luku {number} on alkuluku!")







