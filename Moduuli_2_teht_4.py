#tämä koodi ottaa inputtina käyttäjältä 3 numeroa, ja laskee näiden
#numeroiden summan, tulo, ja keskiarvon

luku_1 = float(input("Syötä ensimmäinen luku: \n"))
luku_2 = float(input("Syötä toinen luku: \n"))
luku_3 = float(input("Syötä kolmas luku: \n"))

def summa(luku_1, luku_2, luku_3):
    return luku_1 + luku_2 + luku_3

def tulo(luku_1, luku_2, luku_3):
    return luku_1 * luku_2 * luku_3

def ka(luku_1, luku_2, luku_3):
    return (luku_1 + luku_2 + luku_3)/3

print(f"Lukujen summa on {summa(luku_1, luku_2, luku_3)}, \
tulo {tulo(luku_1,luku_2, luku_3)} ja keskiarvo {ka(luku_1, luku_2, luku_3)}.")