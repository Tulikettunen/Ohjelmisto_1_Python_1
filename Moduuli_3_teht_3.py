# hemoglobiiniarvo tehtävä, tehty tarkoituksella hieman monimutkaisen kautta,
# jotta vältyttäisiin eri tavoilta ilmaista sukupuoli (nainen/tyttö, mies/poika, jne.)
# kun ei vielä olla opeteltu tehdä valintaruutu tyyppisiä käyttöliittymiä tms.


sukupuoli_nainen = input("Onko biologinen sukupuolesi nainen? (vastaa kyllä/ei): \n")


if sukupuoli_nainen.lower() == "kyllä":
    hemoglobiini_n = int(input("Mikä on hemoglobiinisi?: \n"))
    if hemoglobiini_n < 117:
        print("Hemoglobiinisi on alhainen.")
    elif hemoglobiini_n < 175:
        print("Hemoglobiinisi on normaali.")
    else:
        print("Hemoglobiinisi on korkea.")
else:
    sukupuoli_mies = input("Onko biologinen sukupuolesi mies? (vastaa kyllä/ei): \n")
    if sukupuoli_mies.lower() == "kyllä":
        hemoglobiini_m = int(input("Mikä on hemoglobiinisi?: \n"))
        if hemoglobiini_m < 134:
            print("Hemoglobiinisi on matala.")
        elif hemoglobiini_m < 195:
            print("Hemoglobiinisi on normaali.")
        else:
            print("Hemoglobiinisi on korkea.")
