"""
Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan
tahkojen yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi
21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen nopan
heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
joka kysytään käyttäjältä ohjelman suorituksen alussa.
"""


import random
silmaluku = int(input("Haluttu nopan maximi silmäluku: "))
noppanen = 0


def noppa(x):
    x = silmaluku
    nopp = random.randint(1, x)
    return nopp


while noppanen < silmaluku:
    noppanen = noppa(silmaluku)
    print(noppanen)
