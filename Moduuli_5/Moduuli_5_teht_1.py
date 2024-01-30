"""
Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
Käytä for-toistorakennetta.
"""

import random

dice_amount = int(input("Syötä noppien lukumäärä: \n"))
summa = 0


for dice in range(0, dice_amount):
    noppa = random.randint(1, 6)
    print(noppa)  # trackää toimiiko ohjelma oikein
    summa += noppa


print(f"Noppien silmäluku on: {summa}")
