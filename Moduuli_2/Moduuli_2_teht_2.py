import math

circle_radius = float(input("Syötä ympyrän säde senttimetreinä: \n "))
pii = math.pi

def circle_area(circle_radius):
    return circle_radius**2 * pii

print("Ympyrän pinta-ala on " + str(circle_area(circle_radius)) + " neliösenttimetriä.")