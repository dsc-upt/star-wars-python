print('Hello world!')

"""
Tipuri built-in:
 - chr = char, caracter
 - str = string, siruri de caractere
 - int = integer, intreg
 - float = float, numere reale
 - bool = boolean, True sau False
 - list = ordered and indexed list
 - tuple = ordered and indexed immutable list, lista nemodificabila
 - set = unordered and unindexed list
 - dict = dictionary, dictionar care contine perechi cheie - valoare
"""

cat = "AnaKin"
print(cat)

# type = returneaza tipul variabilei
print(type(cat))

cat = 4
print(type(cat))

print(4 * 5)  # 20: inmultire
print(3 ** 4)  # 81: ridicare la putere
print(14 / 23)  # 0.6086956521739131: returneaza float
print(45 // 4)  # 11: returneaza intreg

integer_var = int('5')  # conversie din string in int
float_var = float('6.8')  # conversie din string in float
print(type(integer_var))
print(type(float_var))

float_var = float(6)
print(type(float_var))
print(float_var)

bool_var = False
print(bool_var)
print(type(bool_var))

#           0  1  2    3        4          5    - indexes
elements = [3, 5, 7, True, "String here", 7.0]  # lists are mutable (modificabile)
#          -6 -5 -4   -3       -2         -1
print(elements[4])
elements.append("New item")  # adaugă un item nou în lista
# elements.insert(3, "Another item")  # add item before a specific index
print(elements)
elements = elements + ["It's house", 5, 'Some " ghilimele']
elements += ["It's house", 5, 'Some " ghilimele']
print(elements)

print(elements[2:6])  # returneaza un substring de la poz 2 pana la 6 (fara cel de pe poz 6)
print(elements[:4])  # returneaza un substring de la inceput pana la 4 (fara cel de pe poz 4)
print(elements[3:])  # returneaza un substring de la poz 3 pana la final
print(elements)
# returneaza un substring de la 3 pana la 10 cu pasul 3
print(elements[3:10:3])

elements = [3, 5, 7, True, "String here", 7.0]  # lists are mutable (modificabile)
#          -6 -5 -4   -3       -2         -1
print(elements[-5:-2])
print(elements[-2:-5:-1])
print(elements[5:2:-1])
print("elements" * 3)  # printează lista de 3 ori