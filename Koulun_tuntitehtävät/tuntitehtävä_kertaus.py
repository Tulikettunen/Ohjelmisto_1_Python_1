lista1 = [1, 5, 'Juha', 3.14, [2, 5], (1, 2, 8), {'eka': 4, 'toka': False}]

print(lista1[6])
print(lista1[-1])

numbers = [12, 5, 21, 4, 8, 0, 11]

#list comprehension
# newlist = [expression for item in iterable if condition == True]
#newlist = [str() for x in lista if x%2==0 in x]


def double(listname):
    return [x*2 for x in listname]


print(numbers)
print(double(numbers))

lista2 = [15,1, 8, 18, 33, 1, 2]


def rajattu_lista(lista):
    min = int(input("syötä min arvo: \n"))
    max = int(input("Syötä max arvo: \n"))
    uuslista = [x for x in lista if x in range(min, max + 1)]
    print(uuslista)
    return sum(uuslista)


print(lista2)
print(rajattu_lista(lista2))