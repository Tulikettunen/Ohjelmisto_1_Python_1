#muuntaa tuumia senttimetreiksi, kunnes käyttäjä antaa negatiivisen luvun

tuumat = float(input("Anna tuumat jotka haluat muuntaa: \n"))

while tuumat >= 0:
    sentit = tuumat * 2.54
    print(f"{tuumat} tuumaa on {sentit} senttiä.")
    tuumat = float(input("Anna tuumat jotka haluat muuntaa: \n"))
