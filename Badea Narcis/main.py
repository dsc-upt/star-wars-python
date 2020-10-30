print("Hello world")


"""
Tipuri built-in:
    -chr = char
    -str = string
    -int = integer
    -float = float
    -bool = boolean
    -list = lista
    -tuple = immutable list, lista nemodificabila
    -set = unordered and unindexed list
    -dict = dictionary
"""


cat="Anakin"
print(cat[3])

# type = returneaza tipil variabilei
print(type(cat))

cat =4
print(type(cat))

print(4 * 5) # 20 inmultire
print(3 ** 4) # 81 ridicare la putere
print(14 / 23) # 0.6086956521739131 returneaza float
print(45 // 4) # 11 returneaza un intreg

integer_var = int('5') # conversie din string in int
float_var = float('6.8') # conversie din string in float
print(type(integer_var))
print(type(float_var))

bool_var = False
print(type(bool_var))
print(bool_var)
#           0  1  2   3        4      5
elements = [3, 5, 7, True, "String", 7.0] # list are mutable
#          -6  -5 -4  -3     -2       -1

print(elements)
print(elements[4])
elements.append("New item") # adauga un item nou in lista

print()
# elements.insert(3, "Another item") # add item befor a specific index
print(elements)

elements += ['added item', 5, 7]
print(elements)

print(elements[2:6]) # returneaza un substring de la pozitia 2 pana la 6(fara cel de pozitia 6)
print(elements[:4]) # returneaza un substring de la inceput pana la 4(fara cel de pozitia 4)
print(elements[3:]) # returneaza un substring de la poz 4 pana la final
print(elements[3:10:3]) # returneaza un substring de la 3 la 10 cu pasul 3

elements = [3, 5, 7, True, "String", 7.0]
print(elements[-5:-2])
print(elements[-2:-5:-1])
print(elements * 3) # printeaza lista de 3 ori
