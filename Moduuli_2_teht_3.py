#suorakulmion piiri ja pinta-ala

kanta = input("Syötä suorakulmion kannan mitat: \n")
korkeus = input("Syötä suorakulmion korkeus: \n")

def pinta_ala(kanta,korkeus):
    return(str(float(kanta) * float(korkeus)))

def piiri(kanta,korkeus):
    return(str(float(kanta)*2 + float(korkeus)*2))

print(f"Suorakulmion pinta-ala on {pinta_ala(kanta,korkeus)} \
eliösenttimetriä ja piirin pituus {piiri(kanta,korkeus)} senttimetriä")
