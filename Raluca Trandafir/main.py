print("Hello people!")
print('Hello world!')

"""
Tipuri built-in:
- chr = char, caracter
- str = string, siruri de caractere
- int = integer, intreg
- float = float, numere reale
- bool = boolean , True sau False
- list = ordered and indexed list
- tuple = ordered and indexed immutable list, lista nemodificabila
- set = unordered and unindexed list, nu se stie ce elemente ne pica 
- dict = dictionary, dictionar care contine perechi cheie - valoare

"""
cat = "Anakin"
print(cat[3])
print(cat.lower())

# type = returneaza tipul variabilei
print(type(cat))

cat = 4
print(cat)
print(type(cat))

print(4 * 5) # 20: inmultire
print(3 ** 4) # 81: ridicare la putere
print(14 / 23) # 0.6086956521739131: impartire de nr. reale -returneaza float
print(45 // 4) # 11: impartire fara rest - returneaza intregul


def function():
    abracadabra = "something"
    print('hello')
    print(abracadabra)


function()
# e frumos sa scriem cu _ numele de variabile, nu cu litere mari, nu gen integerVar. la clase folosim IntegerFlefle
integer_var = int('5') # conversie din string in int
float_var = float('6.8') # conversie din int in string
print(type(integer_var))
float_var = 6.7
print(type(float_var))
print(float_var)
float_var = float(6)
print(float_var)

bool_var = True
print(bool_var)
print(type(bool_var))

#Dan zice: daca vrei o lista, iti creezi o lista
elements = []
print(type(elements))
elements = [3, 5, 7]
print(elements)
#nu conteaza ce tip de data pui in lista in Python
#           0  1  2   3     4              5
elements = [3, 5, 7, True, "String here", 7.0 ] # lists are mutable (modificabile)
#           -6 -5 -4 -3    -2             -1
print(elements)
print(elements[4])
elements.append("New item") # adauga un item nou in lista
print()
elements.insert(3, "Another Item") # add item before a specific index
print(elements)

elements = elements + ['Cat\'s name', 5, 7]
print(elements)

print(elements[2:6]) # returneaza un substring de la poz 2 pana la poz 6 (fara cel de pe poz 6)
print(elements[0:4]) # returneaza un substring de la inceput pana la poz 4 (fara cel de pe poz 4)
print(elements[:4]) # syntactic sugar
print(elements[3:])
print(elements[3:10:3])# returneaza un substring de la 3 pana la poz 10 cu pasul 3
elements = [3, 5, 7, True, "String here", 7.0 ] # lists are mutable (modificabile)
#           -6 -5 -4 -3    -2             -1
print(elements[-5:-2])
print(elements[-2:-5:-1]) # arata in ordine inversa
print(elements[5:2:-1])

print(elements * 3) # printeaza de 3 ori aceasta lista
print("elements" * 3)
print("I am writing in pythoon hoho" )