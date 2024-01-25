#karkausvuosi laskuri

vuosiluku = int(input("Anna vuosiluku niin tarkistan onko se karkausvuosi: \n"))

if vuosiluku % 400 == 0:
    print(f"Vuosiluku {vuosiluku} on karkausvuosi.")
elif vuosiluku % 4 == 0 and vuosiluku % 100 != 0:
    print(f"Vuosiluku {vuosiluku} on karkausvuosi.")
else:
    print(f"Vuosiluku {vuosiluku} ei ole karkausvuosi.")
