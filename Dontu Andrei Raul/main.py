print('Hello World')

"""
Tipuri built-in
-chr= char, caracter
-str = string, siruri de caractere
-int = integer, intreg
-float = flaoat, numere reale
-bool = boolean, True sau False
-list = ordered and indexed lista, cum leai adaugat asa le va afisa si poti sa accesezi orice element
-tuple = ordered and indexed immutable list, lista nemodificabila 
-set = unordeted and unindexed list, nu poti sa accesezi elementele din el 
-dict = dictionary, dictionar care contine  perechi cheie - valoare
"""

cat = "Anakin"
print(cat)

# type = returneaza tipul variabilei(asta ii comentariu pe un singur rand)
print(type(cat))

cat =4
print(type(cat))
print(4 * 5) # 20: inmultire
print(3 ** 4) # 81: ridicare la putere
print(14 / 23) # 0.6086956521739131: impartire float
print(45 // 4) # 11: impartirea fara rest

integer_var = int("5") # conversie din string in int
float_var = float("6.8") # conversie din string in float
print(type(integer_var))
print(type(float_var))

float_var = float(6)
print(type(float_var))
print(float_var)

bool_var = False
print(type(bool_var))
print(bool_var)

#          0  1  2   3        4           5    - indexe
elements =[3, 5, 7, True, "String here", 7.0] # list are mutable(modificabile)
#         -6 -1 -2   -3        -2           -1
print(elements)
print(elements[4])
elements.append("New item") # adauga un item in lista

print()
elements.insert(3, "Another item") # adauga elemente la o pozitie anume
print(elements)

elements = elements + ["It's house",5, 'some " ghilimele' ]
elements += ["It's house",5, 'some " ghilimele' ] # scurtatura
print(elements)

print(elements[2:6]) # returneaza un sustring de la poz 2 pana la 6 (fara cel de pe poz 6)
print(elements[:4]) # returneaza un sustring de la inceput pana la 4 (fara cel de pe poz 4)
print(elements[3:]) # returneaza un sustring de la poz 3 pana la final
print(elements)
# returneaza un subsir de la 3 pana la 10 cu pasul 3
print(elements[3:10:3])

elements =[3, 5, 7, True, "String here", 7.0] # list are mutable(modificabile)
#         -6 -1 -2   -3        -2           -1
print(elements[-5:-2])
print(elements[-2:-5:-1])
print(elements[5:2:-1])
print("elements\n" * 3) # printeaza de 3 ori
