"""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta
varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.
"""


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
optional_list = (input("Kirjoita haluamasi numero listaan, \
kun et halua lisätä enempää, paina enter: \n"))
opt_list = []


def optional_summa(lis):
    while lis != "":
        try:
            opt_list.append(int(lis))
            lis = input("Kirjoita haluamasi numero: \n")

        except:
            lis = input("Kirjoitathan kenttään vain numeroita: \n")
    opt_summa = 0
    for num in opt_list:
        opt_summa += num
    return opt_summa


def listan_summa(lis):
    summa = 0
    for num in lis:
        summa += num
    return summa


print(f"Itse muokattavan listan summa on: {optional_summa(optional_list)}.")

print(f"Kiinteän listan summa on: {listan_summa(lista)}.")
