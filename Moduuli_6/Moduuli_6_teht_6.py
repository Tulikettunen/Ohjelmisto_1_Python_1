"""
Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan
senttimetreinä sekä pizzan hinnan euroina. Funktio laskee ja palauttaa
pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä
kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa
paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
"""


pizza1_e = int(input("Ensimmäisen pizzan hinta euroina: \n"))
pizza1_cm = int(input("Ensimmäisen pizzan halkaisija senttimetreinä: \n"))

pizza2_e = int(input("Toisen pizzan hinta euroina: \n"))
pizza2_cm = int(input("Toisen pizzan halkaisija senttimetreinä: \n"))


def pizza_vertailu(hinta1, hinta2, halkaisija1, halkaisija3):
    pizza1 = pizza1_e / pizza1_cm
    pizza2 = pizza2_e / pizza2_cm
    if pizza1 < pizza2:
        return("Pizza 1 on parempaa vastinetta rahalle.")
    else:
        return("Pizza 2 on parempaa vastinetta rahalle.")


print(pizza_vertailu(pizza1_e, pizza1_cm, pizza2_e, pizza2_cm))
