"""
Scrieti o functie Python care primeste o lista de numere ca argument si returneaza media acestora

lista = [10, 2, 30, 50, 300, 10]

"""
from functools import reduce

lista = [10, 2, 30, 50, 300, 10]

def calculeaza_media(lista):
    return sum(lista) / len(lista) if lista else 0

media = calculeaza_media(lista)
print("Media este:", media)

# Versiunea 1
lista = [10, 2, 30, 50, 300, 10]
print(sum(lista)/len(lista))

# Versiunea 2
# from functools import reduce
lista = [10, 2, 30, 50, 300, 10]
print(reduce(lambda x, y: x+y, lista)/len(lista))

print(reduce(lambda x, y: x+y, lista)/reduce(lambda x, y: x+y, map(lambda x:1, lista) ))
