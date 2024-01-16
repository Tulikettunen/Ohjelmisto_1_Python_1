#tämä koodi kutsuu randomin netistä,
#ja arpoo sillä 3 numeroisen koodin joiden luvut ovat väliltä 1-9
#ja nelinumeroisen koodin jonka luvut ovat väliltä 1-6

import random

koodi1= ""
koodi2= ""

for i in range(3):
    koodi1 = koodi1 + str(random.randint(0,9))

for i in range(4):
    koodi2 = koodi2 + str(random.randint(1,6))

print(koodi1)
print(koodi2)
