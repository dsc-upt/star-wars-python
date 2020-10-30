print('Hello world!')

"""
Tipuri built-in:
- chr = char, caracter
- str = string, siruri de caractere
- int = integer, intreg
- float = float, numere reale
- bool = boolean, True sau False
- list = ordered and indexed list, lista
- tuple = ordered and indexed immutable list, lista nemodificabila
- set = unordered and unindexed list
- dict = dictionary, dictionar care contine perechi cheie -valoare
"""

cat = "Anakin"
print(cat.lower())

# type = returneaza tipul variabilei
print(type(cat))

cat = 4
print(type(cat))

print(4 * 5)  # 20
print(3 ** 4)  # 81 : ridicare la putere
print(14 / 23)  # 0.6086956521739131 : returneaza float
print(45 // 4)  # 15 : returneaza un intreg

integer_var = int('5')  # conversie din string in int
float_var = float('6.8')  # conversie din string in float
print(integer_var)
print(float_var)

bool_var = True
print(bool_var)

#           0  1  2   3          4         5  - indexes
elements = [3, 5, 7, True, "String here", 7.0]  # lists are mutable
#          -6 -5 -4   -3        -2         -1

print(elements)
print(elements[4])
elements.append("New item")  # adauga un item nou in lista

print()
print(elements.insert(3, "Another item"))  # adauga item inaintea unui index specific
print(elements)

elements = elements + ['Added item', 5, 7]
print(elements)

print(elements[2:6])  # returneaza un substring de la poz 2 pana la 6 (fara cel de pe poz 6)
print(elements[:4])  # returneaza un substring de la inceput pana la poz 4 (fara poz 4)
print(elements[3:])  # returneaza un substring de la poz 3 pana la final
print(elements)

# returneaza un substring de la poz 3 pana la 10 cu pasul 3
print(elements[3:10:3])
print(elements[-5:-2])
print(elements[5:2:-1])
print(elements * 3)  # printeaza lista de 3 ori

