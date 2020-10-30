print("hello word")


"""
Tipuri buit-in:
 - chr = char , caracter 
 - str = string, siruri de caractere 
 - int = integer, intreg
 - float = float, numere reale
 - bool = boolean, True sau false
 - list = ordered and indexed lista
 - tuple = ordered and indexed innmutable list
 - set = unordered and unindexed list
 - dic = dictionary, care contine perechi cheie - valoare
"""

cat = "Anakin"
print(cat)
print(cat.lower())

# type = returneaza tipul variabilei
print(type(cat))
cat = 4
print(type(cat))

print(4 * 5) # 20: inmultire
print(3 ** 4) # 81: ridicare la putere
print(14 / 23) # 0.608: impartire
print(45 // 4) # 11: returneaza un intreg

integer_var = int("5")
float_var = float ("6.8")
print(type (integer_var))
print(type (float_var))

bool_var = False
print(bool_var)

elements = [3, 5, 7 ,True , "String here" , 7.0 ] # Lists are mutable
print(elements)
print(elements[4])
elements.append("New item")
print()
print(elements)
print(elements.insert(3, "Another item")) # add item before a specific index
print (elements)

elements = elements + ["Added item", 5, 7]
print(elements)


def function():
    abracadabra = "something"
    print(abracadabra)

function()
print(elements[2:6]) # returneaza un substring de la poz 2 pana la 6 fara ultimul
print(elements[:6])
print(elements[1:])

print(elements[3:9:3]) # elemente de l 3 la 9 din 3 in teri
print(elements[-2:-5:-1])
print(elements[5:2:-1])

print(elements * 3)

