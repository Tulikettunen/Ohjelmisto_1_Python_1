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
    #testataan saatiinko uusi paras tulos, päivitetään edon
    # täyttyessä parhaan pelaajan ja tuloksen arvot muuttujiin best_player ja best_result
    if result > best_result:
        best_result = result
        best_player = current_player
    print(f"pelaajan {current_player}, tuos:{result}")
    current_player += 1
print(f"Paras tulos ja pelaaja: pelaaja {best_player}, tulos {best_result}")