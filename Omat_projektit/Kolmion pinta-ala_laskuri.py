"""
yritys rakentaa ohjelma joka ottaa vaihtoehtoiset 2 arvoa kolmesta,
ja laskee puuttuvan arvon suorakulmaisen kolmion pinta-alasta.
EI TOIMI VIELÄ
"""

print("Jos haluat laskea suorakulmaisen kolmion pinta-alan, /n sivun \
tai korkeuden, syötä 2 arvoa, ja tuntemattoman arvon tilalle 0. \n\n")

korkeus = float(input("syötä kolmion sivun korkeus:\n"))
kanta = float(input("syötä kolmion kannan pituus:\n"))
pinta_ala = float(input("syötä kolmion pinta-ala:\n"))

while True:
    try:
        korkeus >= 0 and kanta >= 0 and pinta_ala >= 0


        def laskuri(ala, kork, kant):
            if pinta_ala == 0:
                print(f"Kolmion pinta-ala on {kanta * korkeus / 2}")
            elif korkeus == 0:
                print(f"Kolmion korkeus on {2 * pinta_ala / kanta}")
            elif kanta == 0:
                print(f"kolmion kanta on {2 * pinta_ala / korkeus}")

    except ValueError:
        print("Syötäthän kenttään vain positiivisia lukuja")

# while True:
#    try:
#        korkeus >=0 or kanta >=0 or pinta_ala >= 0
#
#        if pinta_ala == 0:
#            print("Kolmion pinta-ala on " + kanta * korkeus / 2 )
#        elif korkeus == 0:
#            print( " Kolmion korkeus on " + 2 * pinta_ala / kanta)
#        elif kanta == 0:
#            print(" kolmion kanta on " + 2 * pinta_ala / korkeus)

