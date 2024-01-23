kalan_pituus = float(input("Kuinka pitkä on kalastamanne kuha: \n"))

if kalan_pituus < 37:
    print(f"Kalastamanne kuha on alimittainen {37 - kalan_pituus} centtimetrillä, \
    päästäthän sen vapaaksi")
else:
    print(f"Kalastamanne kuha on riittävän iso, saatte pitää sen!")

