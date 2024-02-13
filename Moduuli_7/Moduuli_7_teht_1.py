"""
Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen
ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina
monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden
mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.
"""

vuodenajat = ("Talvi", "Kevät", "Kesä", "Syksy")

käyttäjän_kuukausi = 2

while type(käyttäjän_kuukausi) == str or käyttäjän_kuukausi >= 1 or käyttäjän_kuukausi <= 12:
    käyttäjän_kuukausi = input("Anna kuukauden numero: \n")

    try:
        käyttäjän_kuukausi = int(käyttäjän_kuukausi)
        if käyttäjän_kuukausi in range(3, 6):
            print(f"Vuodenaika on {vuodenajat[1]}")
            break
        elif käyttäjän_kuukausi in range(6, 9):
            print(f"Vuodenaika on {vuodenajat[2]}")
            break
        elif käyttäjän_kuukausi in range(9, 12):
            print(f"Vuodenaika on {vuodenajat[3]}")
            break
        elif käyttäjän_kuukausi == 12 or käyttäjän_kuukausi in range(1, 3):
            print(f"Vuodenaika on {vuodenajat[0]}")
            break
        else:
            print("Oot idiootti, vuodes on vaa 12 kuukautta :P ")
    except Exception as e:
        print("Oletpa typerä, kirjain ei ole kuun numero. Anna validi luku")
