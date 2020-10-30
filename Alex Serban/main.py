print('Hello world!')

"""
Tipuri built-in:
- chr = char, caracter
- str = string, sir de caractere
- int = integer, intreg
- float = float, numere reale
- bool = boolean, True sau False
- list = ordered and indexed list
- tuple = ordered and indexed immutable list, lista nemodificabila
- set = unordered and unindexed list
- dict = dictionary, dictionar care contine perechi cheie - valoare
"""

cat = "AnaKin"
print(cat.lower())

#type = returneaza tipul variabilei
print (type(cat))

cat = 4
print(type(cat))

print(4 * 5)   # 20 -> inmultire
print(3 ** 4)   # 81 -> ridicare la putere
print(14 / 25)   # 0.56 -> impartire de nr reale
print(45 // 4)   # 11 -> impartire de intregi

# definirea unei functii:
def function ():
    print("Hey")
    lmao = "lmao"
    print(lmao)
# ce nu mai are tab nu intra in functie, aici functioneaza pe baza de indentare

function()

# conversie din string in int / float:
int_var = int ('5')
float_var = float('6.8')
print(int_var)
print(float_var)

float_var = 5.7
print(float_var)
print(type(float_var))

bool_var = False
print(bool_var)
print(type(bool_var))

# lista:
#           0  1  2   3        4           5       = indexes
elements = [3, 5, 7, True, "string here", 7.8]  #lists are mutable (modificabile)
print(type(elements))
print(elements[4])

elements.append("New item") # adauga un item nou in lista
print()

elements.insert(3, "Another item") # adauga item nou inainte de pozitia specificata (3)
print(elements)

elements = elements + ['let myself go', "it's house", 'every "weekend"'] #concatenare de 2 liste
# elements += ['let myself go', "it's house", 'every "weekend"'] -> sintactic sugar
print(elements)

print(elements[2:6])    # returneaza substring de la pozitia 2 pana la 6 (fara cel de pe pozitia 6)
print(elements[:4])     # returneaza substring de la inceput pana la 4 (fara cel de pe pozitia 4)
print(elements [3:])    # returneaza substring de la pozitia 3 pana final (fara cel de pe pozitia 6)
print(elements)
print(elements[3:10:3])   # returneaza un substring de la 3 pana la 10 cu pasul 3

elements = [3, 5, 7, True, "string here", 7.8]
#          -6  -5 -4  -3        -2         -1
print()
print(elements)
print(elements[-5:-2])
print(elements[-2:-5:-1])
print(elements[::-1])
print(elements[5:2:-1])
print(elements * 3)     #printeaza lista de 3 ori