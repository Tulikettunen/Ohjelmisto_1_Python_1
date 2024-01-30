# yksinkertainen funktio, ei palauta mitään
def do_something():
    print("Doing something")


do_something()

print("Some other code")


def calculate_numbers(num1, num2):
    print(f"{num1 + num2}")

# sum = calculate_numbers(2,3)
# print(f"summa{sum}")               #palauttaa "summaNone"


def calculate_numbers2(num1, num2):
    return num1 + num2


summa = calculate_numbers2(2, 3)
print(f"Summa = {summa}")


def calculate_numbers3(calc_type, num1, num2):
    if calc_type == "add":
        return num1 + num2
    elif calc_type == "multiply":
        return num1 * num2
    return "No such calculation type"


calculate_numbers3("add", 2, 3)
print(f"Summa: {calculate_numbers3('add', 2, 3)}")

nro_summa = calculate_numbers3("add", 2, 3)
print(f"Summa: {nro_summa}")
print(f"Tulo: {calculate_numbers3('multiply', 2, 3)}")


def calculate_numbers_list(calc_type, numbers):  # muuttujat on esitelty funktiossa, muuttujat ei
    if calc_type == "add":                      # käytössä missään ulkopuolella
        # numbers_sum = sum(numbers)
        nummers_summ = 0
        for num in numbers:
            nummers_summ += num
        return nummers_summ
    elif calc_type == "multiply":
        nummers_multiply = 1
        for num in numbers:
            nummers_multiply = nummers_multiply * num
        return nummers_multiply
    return "No such calculation type"


nroiden_summa = calculate_numbers_list("add", [1, 2, 3, 4, 5])
print(f"Listan Summa: {nroiden_summa}")
print(f"Listan Tulo: {calculate_numbers_list('multiply', [1, 2, 3, 4, 5])}")


# lista parametrina (viittaus)
inventory = ["kynä", "kumi"]


def add_stuff(item):        # item on parametri
    inventory.append(item)
    print("Reppuun lisättiin " + item)
    return inventory


add_stuff("tietokone")
print(inventory)


def add_stuff2(item, new_inventory):        # item on parametri
    new_inventory.append(item)
    print("Reppuun lisättiin " + item)
    return new_inventory


print(add_stuff2("tietokone", inventory))    # esimerkki mutatoinnista
print(inventory)
# inventory on alkuperäinen laatikko, new_inventory on vain funktion sisällä toimiva pala
# ja muuttaa alkuperäisetä listaa, koska vanha lista on viittaus uuteen


# materiaaliesimerkki primitiiviarvoilla
def vaihda(kaupunki):
    kaupunki = "Vantaa"
    print("Funktiossa lopuksi: " + kaupunki)
    return


kaupunki = "Helsinki"
print("Pääohjelmassa aluksi: " + kaupunki)
vaihda(kaupunki)
# alkuperäinen muuttujan arvo ei muuttunut
print("Pääohjelmassa lopuksi: " + kaupunki)
print(kaupunki)


# nimetyt parametrit
# nyt calc_typelle on määritelty oletusarvo, eli jos sitä ei määritellä erikseen, oletusarvo on add
# valinnainen parametri sijoitettava loppuun, jotta määriteltävät tulevat ensin, niinkuin
# integroiduissa funktioissa
def calc_v2(num1, num2, calc_type="add"):
    if calc_type == "add":
        return num1 + num2
    elif calc_type == "multiply":
        return num1 * num2


result = calc_v2(1, 2)
print(result)
print(calc_v2(1, 2, "multiply"))
# syötetään parametrit vapaassa järjestyksessä nimeämällä ne
result = calc_v2(num2=5, num1=2, calc_type="multiply")


# satunnainen määrä parametreja
def list_numbers(*parameters):
    # parameters sisältää kaiki annetut parametrien arvot yhetenä monikkona
    # ("kiinteä" lista, tuple
    return parameters


print(list_numbers(3, 5, 7, "kutonen"))
