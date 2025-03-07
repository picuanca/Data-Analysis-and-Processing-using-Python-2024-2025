"""
Definiti o functie care primeste un string ca argument si returneaza un nou dtring in care toate vocalele au fost eliminate

vocale = "aeiouAEIOU" 
input_string = "Salutare, ce mai faci?" 
"""

vocale = "aeiouAEIOU"
input_string = "Salutare, ce mai faci?"

# Varianta 1
def elimina_vocale(ch):
    return ch not in vocale
print("".join((filter(elimina_vocale, input_string))))

# Varianta 2 
print("".join((filter(lambda x: x not in vocale, input_string))))

# Varianta 3 - list comprehention
print("".join([ch for ch in input_string if ch not in vocale]))



