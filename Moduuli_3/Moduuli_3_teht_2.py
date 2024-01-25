#hyttiluokka tehtävä

asiakkaan_hyttiluokka = input("Mikä hytti luokka teillä on?: \n")

if asiakkaan_hyttiluokka.upper() == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella")
elif asiakkaan_hyttiluokka.upper() == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella")
elif asiakkaan_hyttiluokka.upper() == "B":
    print("B on ikkunaton hytti autokannen yläpuolella")
elif asiakkaan_hyttiluokka.upper() == "C":
    print("C on ikkunaton hytti autokannen alapuolella")
else:
    print("Virheellinen hyttiluokka")