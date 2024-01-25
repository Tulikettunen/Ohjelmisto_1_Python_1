#tämä tehtävä laskee painon vanhanaikaisina mittoina ilmoitettuna
#leivisköistä, nauloista ja luodeista kilogrammoiksi ja grammoiksi



gramma= 1
luoti = float(input("Anna luodit: \n")) *13.3
naula = float(input("Anna naulat: \n")) *32 * luoti
leiviskä = float(input("Anna leiviskät: \n")) *20 * naula

def paino_grammoina(leiviskä,luoti,naula):
    return (luoti + naula + leiviskä) % 1000
def paino_kiloina(leiviskä,luoti,naula):
    return (gramma + luoti + naula)*10**-3

print(f"Painosi nykymitoilla on: \n{int(paino_kiloina(leiviskä,luoti,naula))}kg\
ja {round(paino_grammoina(leiviskä,luoti,naula), 2):.2f}g.")