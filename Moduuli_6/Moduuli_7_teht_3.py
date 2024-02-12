"""
Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma
kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn
lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman
syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan
lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti,
kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja
helposti selaimen avulla.)
"""


import mysql.connector


connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)
set_lentokentät = set()
dict_lentokentät = {}

def kenttä_add(icao):
    icao = input("Syötä lentokentän koodi: \n")
    cursor = connection.cursor()
    cursor.execute(f"SELECT airport.name, airport.ident FROM airport WHERE airport.ident = '{icao}';")
    if cursor.rowcount == 0:
        print("Hakemaasi lentokenttää ei ole olemassa.")
    elif cursor.rowcount == 1:
        if cursor.fetchone() in dict_lentokentät:
            print("Hakemasi lentokenttä on jo tallennettu.")
        else:
            dict_lentokentät[f"{icao}"] = cursor.fetchone()
            print("Uusi lentokenttä lisätty kirjastoon")
    else:
        print("Useampi hakutulos, tarkenna hakua")
    return

def kenttä_haku(icao):
    icao = input("Syötä lentokentän koodi: \n")
    print(dict_lentokentät[icao])

while True:
    choice = input("Jos haluat hakea tietoa: "
                   "valitse 1. \n Jos haluat lisätä uuden: valitse 2. "
                   "\nJos haluat lopettaa: paina 3: \n")
    if int(choice) == 1:
        ICAO = input("Syötä kentän ICAO-koodi: \n")
        print(f"Hakemasi kenttä: {kenttä_haku()}")
    elif int(choice) == 2:
        ICAO = input("Syötä kentän ICAO-koodi: \n")
        kenttä_add(ICAO)
    elif int(choice) == 3:
        False

    else:
        choice = input("Syötäthän jonkun numeron 1-3!\n"
                        "Jos haluat hakea tietoa: valitse 1. \n "
                        "Jos haluat lisätä uuden: valitse 2. \n"
                        "Jos haluat lopettaa: paina 3: \n")

while True:
    choice = input("os haluat hakea tietoa: valitse 1 \n"
                   "Jos haluat lisätä uuden: valitse 2 \n"
                   "Jos haluat lopettaa: paina 3: \n")
    match choice:
        case "1":
            ICAO = input("Syötä kentän ICAO-koodi: \n")
            print(f"Hakemasi kenttä: {kenttä_haku()}")
        case "2":
            ICAO = input("Syötä kentän ICAO-koodi: \n")
            kenttä_add(ICAO)
        case "3":
            break

