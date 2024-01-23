#while loop

#jakolaskukone
"""
num1 = float(input("Enter a number: \n"))
num2 = float(input("Enter a second number: \n"))

if num2 == 0:
    print("Et voi jakaa nollalla, anna uusi luku")
    num1 = float(input("Enter a valid number: \n"))
division = num1 / num2

print(division)

num1 = float(input("Enter a number: \n"))
num2 = float(input("Enter a second number: \n"))

while num2 == 0: # or str???
    print("Et voi jakaa nollalla, anna uusi luku")
    num2=float(input("Enter a valid number: \n"))

division2 = num1 / num2

print(f"Division is: {division2}")

#iteroiva loop, käytetään "laskuria" silmukakn toitokertojen määrittelyyn

#print("numero on 1")
#print("numero on 2")
#print("numero on 3")
#print("numero on 4")

#iteraatio, oma versio ennen opettajan ohjetta
num = 1
while num <= 6:
    print(f"numero {num + 1}")

#seuraava versio iteraatiolla, opettajan versio
i = 1
while i < 11:
    print(f"numero {i}")
    i += 1

print(f"ii:n arvo lopulta on {i}")
"""

#seuraava versio käyttäjän syötteellä
i = int(input("From which number you wanna start from?: \n")) #iteraattori/lähtönumero
amount = int(input("Enter amount of repeat: \n"))
offset = int(input("Millä välityksellä haluat numerot?: \n"))
max_number = amount * offset
while i <= max_number:  #max_number = amount + i
    print(f"numero {i}")
    i += offset

print(f"ii:n arvo lopulta on {i}")