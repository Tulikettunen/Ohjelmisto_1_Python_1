"""
Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy
gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa
hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
Yksi gallona on 3,785 litraa.
"""

gallonat = int(input("Gallonat jotka haluat muuttaa litroiksi: \n"))


def litroiksi(x):
    result = x * 3.785
    return result


while gallonat >= 0:
    print(litroiksi(gallonat))
    gallonat = int(input("Gallonat jotka haluat muuttaa litroiksi: \n"))
