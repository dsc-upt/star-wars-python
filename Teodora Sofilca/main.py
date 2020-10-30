print("Hello world")


"""
comentariu
pe mai
multe 
randuri

Tipuri built-in:
-chr = caracter
-str  = string, siruri de caractere
-int  = integerm intreg
-float = float, numere reale
-bool = boolean, true/false
-list = lista, ordonata si indexata
-tuple = lista nemodificabila, ordonata si indexata, immutable list
-set = lista neordonata si neindexata
-dic = dictionary, dictionar care contine perechi cheie - valoare
"""

cat = "Anakin"

print(cat.lower())
# type = returneaza tipul variabilei

cat = 4
print(type(cat))

print(4*5)
print(3**4)  # ridicare la putere
print(14/23)
print(45//4)  # impartire fara rest

def function():
      print("hello")


function()

integer_var = int('5')
float_var = float('6.8')
print(type(integer_var))
print(type(float_var))

bool_var = True
print(bool_var)
print(type(bool_var))

#           0  1  2    3     4        5 - indexes
elements = [3, 5, 7, True, "string", 7.8]  # lists are mutable/modificabile
#           -6 -5 -4   -3     -2      -1
print(type(elements))
print(elements[4])

# elements.append("New item")  # adauga item nou in lista
print()
print(elements)

print(elements.insert(7, "Another item"))  # add item before a sfecific item
print()
print(elements)

elements = elements+['Added item', 5, 7]
print(elements)

print(elements[2:6])    # intre 2 si 6
print(elements[:4])     # primele 4 fara 4
print(elements[3:])     # de la 3 la final
print(elements[3:9:2])  # de la 3 la 9 cu pasul 2


elements = [3, 5, 7, True, "string", 7.8]
print(elements[-5:-2])
print(elements[-2:-5:-1])

print(elements * 3)  # printeaza lista de 3 ori
