print('Hello world')

#tipuri built-in
"""
    - str = string
    - chr = char
    - int = integer
    - float
    - bool
    - list = ordered and indexed list
    - tuple = ordered and indexed lista nemodificabila
    - set = unordered and unindexed list
    - dict = dictionary, dictionar care contine perechi cheie - valoare
"""

cat = "Anakin"
print(cat)

#type = returneaza tipul variabilei
print(type(cat))

cat = 4
print(type(cat))

print(4 * 5)
print(3 ** 4)
print(14 / 23)
print(45 // 3)

#variabile - bam_bam
#clase - BamBam

integer_var = int('5') #conversie string in int
float_var = float('6.8') #conversie string in float
print(integer_var)
print(float_var)

bool_var = True
print(bool_var)
print(type(bool_var))

elements = [3, 5, 6, True, "string", 7.0] #lists are mutable
print(type(elements))
print(elements[3])
elements.append("New item") #adauga un item in lista
elements.insert(3, "Another item") # add item before index 3
print()
print(elements[3])
elements = elements + ['Added item', 5, 7]
print(elements)










