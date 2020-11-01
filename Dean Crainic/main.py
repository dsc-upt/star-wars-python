print("Hello World")

"""
Tipuri build-in:
 - chr = char, caracter
 - str = string, siruri de caractere
 - int = integer, intreg
 - float = float, numere reale
 - bool = boolean, true sau false
 - list = ordered and indexed lista (practic vector)
 - tuple = ordered and idexed immutable list, lista nemodificabila
 - set = unordered and unindexed list
 - dict = dictionary, dictionar care contine perechi cheie valoare
"""

cat = "Anakin"
print(cat.upper())

# type = afiseaza tipul variabilei
print(type(cat))

cat = 4
print(cat)
print(type(cat))

print(4 * 5) # 20: inmultire
print(3 ** 4) # 81: putere
print(14 / 23) # 0.60...: impartire float
print(45 // 4) # 11: impartire intreg
def function():
    abracadabra = "some"
    print(abracadabra)

function()

integer_var = int('5')
float_var = float('6.8')
print(integer_var)
print(float_var)

elements = [3, 5, 6, True, "String", 7.0] # listele sunt modificabile
print(elements)
print(elements[4])

elements.append("New item") # adauga un item nou in lista
print()
print(elements)

print(elements.insert(3, "Another item"))
print(elements) # adauga un item nou inaintea unui index

elements = elements + ['Added item', 5]
print(elements) # concatenare intre doua liste

print(elements[3:6]) # returneaza de la 3 pana la 6 (fara 6)
print(elements[:3]) # returneaza de la 0 pana la 3 (fara 3)
print(elements[3:]) # returneaza de la 3 pana la  final
print()
print(elements)
print(elements[3:10:3])
print(elements[-5:-2]) # afiseaza la fel, dar numara pozitiile de la dreapta la stanga
print(elements[5:2:-1]) # afiseaza in ordine inversa

print(elements * 3) # printeaza lista de 3 ori