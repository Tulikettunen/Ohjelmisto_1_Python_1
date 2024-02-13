import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)

cursor = connection.cursor()
cursor.execute("SELECT name FROM country")
result = cursor.fetchone()  #fetchone hakee yhden rivin kerrallaan tulosjoukosta
print(result)
result = cursor.fetchall()  #lista in tässä kohtaa "tyhjä"
print(result)
cursor.execute("SELECT iso_country, name FROM country")
result_row = cursor.fetchall()
print(f"ensimmäinen rivi: {result_row[0]}, jossa maakoodi: {result_row[0][0]}")
print(f"Maakoodeja löytyi {cursor.rowcount} kappaletta")    #kuinka monta riviä löytyy ylipäätään listalta
print(cursor.fetchone())    #tässä kohtaa kursorilla ei ole mitään läpikäytävää jäljellä, joten tulos on None


if cursor.rowcount > 0: #tarkistaa että onko rivejä joita printata, ja printtaa vain jos on
    for row in result_row:
        print(f"Maakoodi: {row[0]}, nimi: {row[1]}")
else:
    print("Ei tuloksia.")


cursor.execute("SELECT iso_country, name FROM country WHERE name = 'Finland'")
result_row = cursor.fetchall()

if cursor.rowcount > 0: #tarkistaa että onko rivejä joita printata, ja printtaa vain jos on
    for row in result_row:
        print(f"Maakoodi: {row[0]}, nimi: {row[1]}")
else:
    print("Ei tuloksia.")

#parempi tapa: kääritään yskittäiset toiminnallisuudet uudelleenkäytettäviin funktioihin


def find_country_by_code(iso_code):
    sql = f"SELECT name, continent FROM country WHERE iso_country = '{iso_code}'"   #valitsee iso_coutry \
                                            # taulusta sarakkeet name ja continent, jossa maakoodi on valinnainen
    cursor = connection.cursor()
    cursor.execute(sql)         #tässä kohtaa jo kursori tietää montako riviä on tulossa
    result = cursor.fetchone()
    if cursor.rowcount == 1:
        return result
    return                      #jos if lause ei toteudu, funktio palauttaa None


user_input = input("Anna maakoodi: \n")
country = find_country_by_code(user_input)

#testaa jos countrylla on joku muu arvo kuin none, se on true, ja se lukee koodin
#if country != None
if country:
    print(f"Löydetty maa: {country[0]}, {country[1]}")
else:
    print("Ei tuloksia.")


#____

def update_country_name_by_code(iso_code, name):
    sql = f"UPDATE country SET name='{name}' WHERE iso_country = '{iso_code}'"
    #tarkasta, että sql on oikein muodostettu
    print(sql)
    sursor = connection.cursor()
    cursor.execute(sql)
    if cursor.rowcount == 1:    #tarkistaa onko toiminto mennyt oikein
        print(f"Tietue päivitettu ({iso_code}: {name}).")
        return True
    print("Päivitys epäonnistunut.")

code_input = input("Anna maakoodi:")
country_input = input("Anna uusi nimi:")
update_country_name_by_code(code_input, country_input)

#from geopy import distance #loppu koodi läytyy tehtävien linkistä
