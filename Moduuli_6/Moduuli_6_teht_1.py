"""
Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen
nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa niin
kauan kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
"""
import random
noppanen = 0


def noppa():
    nopp = random.randint(1, 6)
    return nopp


while noppanen < 6:
    noppanen = noppa()
    print(noppanen)
