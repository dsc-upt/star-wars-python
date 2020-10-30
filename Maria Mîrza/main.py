print('Hello world!')

"""
Tipuri de baza(built-in):
-chr= char, caracter
-str= string, siruri de caractere
-int= integer
-float= float, nr reale
-bool= boolean, True || False
-list= ordered and indexed list(cum le adaugi, asa le primesti)
-tuple= ordered and indexed immutable list, lista nemodificabila
-set= unordered and unindexed list
-dict= dictionary, dictionar care contine perechi cheie-valoare

"""

cat="Frufru"
print(cat)
print(cat[3])
print(cat.lower())
print(cat.upper())

# type returneaza tipul variabilei
print(type(cat))

cat=8
print(cat)
print(type(cat))

print(4*5) # 20-inmultire
print(3**4) # 81-ridicare la putere
print(14/23) # 0.6086956521739131- impartire - returneaza float
print(45//4) # 11- returneaza intreg

def function():
    aaa="AAAAA"
    print(aaa)

function()

integer_var=int('5') # conversie din string in int
float_var=float('6.8')
print(type(integer_var))
print(integer_var)
print(type(float_var))
print(float_var)

bool_var=False
print(bool_var)
print(type(bool_var))

#           0  1  2   3       4
elements = [3, 5, 7, True, "STRING"]  # lists are mutable ( modificabile )
print(type(elements))
print(elements)

print(elements[4])

elements.append("New item")  # adaugam un item nou in lista
print()
elements.insert(3, "Another item")  # add item before a specific index
print(elements)

elements=elements+ ['Added item']  # adauga la final
print(elements)

print(elements[2:6])
print(elements[:4])  # ia o sublista de la inceput pana la...
print(elements[3:])  # ia o sublista de la pozitia 3 pana la ultima
print((elements[3:9:3])) # afiseaza elementele din 3 in 3 de la poztia 3 pana la pozitia 9

print(elements[-5:-2])
print(elements[5:2:-1])
print(elements[-2:-5:-1])

print(elements*3) # afiseaza lista de 3 ori
