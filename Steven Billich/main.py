"""pot face comentarii aici calumea
tipul built in :
char-> caracter
str -> string, siruri de caractere
int -> integer, intreg
float -> float, numere reale
bool -> boolean, True sau False
list -> lista
tuple -> lista nemodificabila
set -> unordered and unindexed list
dict -> dictionary, contine cheie si valoare"""
print("Hello World!")

cat = "Anakin"
print(cat)

print(type(cat))
cat = 4
print(cat)

print(4 * 5)
print(3**4)
print(14/23)
print(45//4)


def function():
    print('something')


function()

integer_var = int('5')  # conversie din string in int
print(integer_var)

bool_var = False

elements = [1, 2, 3, True, "String", 7.0]  # list are mutable (modificabile)
print(elements)
elements.append("new item")
print(elements)
elements.insert(3, "Inca ceva")
print(elements)

elements = elements + [1, 5, 7]
print(elements)

print(elements[2:5])
print(elements[3:9:2])
print(elements[-2])  # manevra de la python
print(elements[-1:-6])
