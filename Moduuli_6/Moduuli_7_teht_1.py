"""
Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen
ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina
monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden
mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.
"""

vuodenajat = ("Talvi", "Kevät", "Kesä", "Syksy")

käyttäjän_kuukausi = int(input("Anna kuukauden numero: \n"))

while käyttäjän_kuukausi < 1 or käyttäjän_kuukausi > 12:
    käyttäjän_kuukausi = int(input("Anna validi kuukauden numero: \n"))

if käyttäjän_kuukausi in range(3, 6):
    print(f"Vuodenaika on {vuodenajat[1]}")
elif käyttäjän_kuukausi in range(6, 9):
    print(f"Vuodenaika on {vuodenajat[2]}")
elif käyttäjän_kuukausi in range(9, 12):
    print(f"Vuodenaika on {vuodenajat[3]}")
else:
    print(f"Vuodenaika on {vuodenajat[0]}")

