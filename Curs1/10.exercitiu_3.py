"""
Creati urmatoarea lista intr-o singura linie de comanda
my_list = ["1", "2", "3", "4"]

"""

my_list = ["1", "2", "3", "4"]

my_list = (lambda: list(map(str, range(1, 5))))()
print(my_list)


my_list = list(range(1, 5))
print(my_list)


my_list =list(map(str, range(1, 5)))
print(my_list)


my_list = [str(i) for i in range(1, 5)]
print(my_list)