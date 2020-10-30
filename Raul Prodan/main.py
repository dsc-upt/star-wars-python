print('Hello world!')

"""
Tipuri build-in:
    *chr - char
    *str - string
    *int - integer
    *float - float
    *bool - boolean
    *list - oredered and indexed list
    *tuple - oredered and indexed immutable list, lista nemodificabila
    *set - unoredered and unindexed list
    *dict - dictionary,contine pereche cheie-valoare
"""

cat = "Kity"
print(cat.find('4'))
print(type(cat))  # afisare tipul variabilei

cat = 4
print(cat)
print(type(cat))

print(4 * 5)
print(3 ** 4)
print(14 / 23)
print(45 // 3)


def function():
    print("functie")


function()

integer_var = int('5')
float_vat = float('6.8')
print(integer_var)
print(float_vat)

bool_var = True
print(bool_var)

elements = [3, 5, 7, True, "String here", 7.0]
print(elements)
elements.append("new Items")
elements.insert(3, "poz")
print(elements)

elements += ["ADD", "AT FINAL"]
print(elements[2:6])  # SUBSTRING DE LA 2 PANA LA 6
print(elements[:4])  # SUBSTRING DE LA 0 PANA LA 4
print(elements[3:])  # SUBSTRING DE LA 3 PANA LA FINAL
print(elements[0:9:3])  # de la 0 pana la 9 cu pasul 3
