"""
Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on
syötetty viisi kertaa. Edellisessä tapauksessa tulostetaan Tervetuloa ja
jälkimmäisessä Pääsy evätty. (Oikea käyttäjätunnus on python ja salasana rules).
"""

password = "rules"
username = "python"

i = 1
while i <= 5:
    username_gues = input("Give username: \n")
    password_gues = input("Give password: \n")
    if username_gues == username and password_gues == password:
        print("Tervetuloa!")
        break
    elif username_gues != username or password_gues != password:
        if i < 4:
            print("Salasana tai käyttäjätunnus väärin, kokeile uudestaan.")
        print(f"{5-i} yritystä jäljellä.")
    i += 1
else:
    print("Pääsy evätty.")

