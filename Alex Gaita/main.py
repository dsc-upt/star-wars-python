print('Hello World')

"""
Tipuri built-in:
- char = char, caracter
- str = string ,siruri de caractere
- int = integer, intreg
- float = float ,numere reale
- bool = boolean ,True sau False
- list = lista (ordered and indexed list)
- tuple = lista nemodificabila(immutable list)
- set =  unordered and unindexed list
- dict = dictionary
"""
cat = "Anakin"
print(cat)

cat = 4
print(type(cat))

print(4 * 5)
print(3 ** 4)
print(14 / 23)
print(45 // 4)

integer_var = int('5')  #conversie din string in int
float_var = float('6.8')  #conversie din string in float

print(integer_var)
print(float_var)

bool_var = True
print(bool_var)
print(type(bool_var))

elements = [3, 5, 7, True, "String", 7.0] #lists are mutable
print(type(elements))
print(elements[4])
elements.append("New item") #adauga un item nou in lista
print()

elements.insert(3,"Another item") #adauga un intem inainte de un index
print(elements)

elements = elements + ['It\'s house',5,"Some ' apostrof"]
print(elements)

print(elements[2:6]) # Returneaza un substring de la poz 2 pana la 6 (fara 6)
print(elements[:4]) # Returneaza un substring de la inceput pana la 4 (fara 4)
print(elements[3:]) # Returneaza un substring de la poz 3 pana la final
print(elements)
print(elements[3:10:3]) # Returneaza un substring de la poz 3 pana la 10 cu pasul 3

elements = [3, 5, 7, True, "String", 7.0]
print(elements[-5:-2])
print(elements[-2:-5:-1])
print(elements[5:2:-1])
print(elements*3) #printeaza lista de 3 ori
