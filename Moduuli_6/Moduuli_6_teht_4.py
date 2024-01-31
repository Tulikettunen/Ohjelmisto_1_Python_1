"""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta
varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.
"""


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
optional_list = (input("Kirjoita haluamasi numero: \n"))
opt_list = []


def optional_summa(lis):
    while lis != "":
        opt_list = opt_list.append(int(lis))
        lis = input("Kirjoita haluamasi numero: \n")
    return opt_list


def listan_summa(lis):
    summa = 0
    for num in lis:
        summa += num
    return summa


print(listan_summa(lista))

print(optional_summa(optional_list))
