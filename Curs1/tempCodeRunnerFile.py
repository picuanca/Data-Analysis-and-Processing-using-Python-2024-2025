from functools import reduce
lista = [10, 2, 30, 50, 300, 10]
print(reduce(lambda x, y: x+y, lista))