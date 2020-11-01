print('Hello world!')

"""
tipuri built-in:
- chr = cha, carcater 
- str = string, siruri de caractere
- int = integer,intreg
- float = float , numere reale
- bool = boolean, True sau False
- list = ordered and indexed lista
- tuple = ordered and indexed immutable list, lista nemodificabila
- set = unordered and unindexed list
- dict = dictionary, dictionar care contine perechi cheie - valoare
"""

cat = "Anakin"
print(cat.lower())

# type = returneaza tipul variabilie
print(type(cat))

cat = 4
print(type(cat))

print(4 * 5)  # 20: inmultire
print(3**4)  # 81: ridicare la putere
print(14 / 23)  # 0: returneaza float
print(45 // 4)  # 15: returneaza intreg

def function():
    abacadabra = "something"
    print(abacadabra)


function()

integer_var = int('5')  # coversie din string in int
float_var = float('6.8')  # coversie din string in float
print(type(integer_var))
print(type(float_var))

float_var = float(6)
print(type(float_var))
print(float_var)

bool_var = False
print(bool_var)
print(type(bool_var))

#           0  1  2    3      4            5
elements = [3, 5, 7, True, "string here", 7.0]  #lists are mutable (modificabile)
#          -6 -5 -4   -3         -2        -1
print(elements[4])
elements.append("New item")  #adauga un item nou in lista

#  elements.insert(3, "another item")  #add item before a specific index
print(elements)

elements = elements + ['it\'s house', 5, 7]
elements += ['it\'s house', 5, 7]
print(elements)

print(elements[2:6])  # returneaza un substring de la poz 2 pana la poz 6 (fara cel de pe poz 6)
print(elements[:4])   # returneaza un substring de la inceput pana la 4 ( fara cel de pe poz 4)
print(elements[3:])   # returneaza un substring de la poz 3 pana la final
print(elements)
print(elements[3:10:3])  # returneaza un substring de la 3 pana la 10 cu pasul 3

elements = [3, 5, 7, True, "string here", 7.0]  #lists are mutable (modificabile)
#          -6 -5 -4   -3         -2        -1
print(elements[-5:-2])
print(elements[-2:-5:-1])
print(elements[5:2:-1])
print(elements * 3)