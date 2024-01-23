#sisäkkäiset kontrollirakenteet ja satunnaisuus
"""
import random
rand_num = random.randint(1,2)
print(f"Arvottu numero {rand_num}")
"""

player_count = int(input("How many players: \n"))
dice_amount = int(input("How many dices: \n"))
dice_count = 1

best_player = None
best_result = 0

#jokainen pelaaja suorittaa vuorollaan
current_player = 1
while current_player <= player_count:
    result = 0  #nopan silmälukujen summa ennen heittoja
    throw_count = 0
    while throw_count < dice_amount:
        dice = random.randint(1,6)
        result = result + dice
        print(f"pelaajan {current_player}, {throw_count}. heitto: {dice}")
        result += dice
        throw_count += 1
    print(f"pelaajan {current_player}, tuos:{result}")
    #testataan saatiinko uusi paras tulos, päivitetään edon
    # täyttyessä parhaan pelaajan ja tuloksen arvot muuttujiin best_player ja best_result
    if result > best_result:
        best_result = result
        best_player = f"pelaaja {current_player}"
    elif result == best_result: #jos tulos ei parempi mut yhtäsuuri, lisätään 2 pelaajan nro
        best_player = best_player + f"Pelaaja {current_player}"
    current_player += 1
print(f"Paras tulos ja pelaaja: pelaaja {best_player}, tulos {best_result}")


#Break_komento, "heittää" ulos aktiivisesta silmukasta, suoritus jatkuu koodilohkon jälkeen

counter = 0
while True: #ikuinen silmukka
    print(f"laskuri eka {counter}")
    counter += 1
    if counter == 8:
        break   #poistuu silmukan koodilohkosta samantien, alla oleva ei toistu
    print(f"laskuri toka {counter}")

