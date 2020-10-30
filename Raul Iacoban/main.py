"""
tipuri built-in
chr
str
int
float
bool
list - ordered and indexed list
tuple - ordered and indexed immutable list
set - unordered and unindexed list
dict - dictionary, contains pairs of key - value
"""

var = "jake"
print(var[1])
print(type(var))

var = 5
print(var)
print(type(var))

print(2**3)
print(28/3)
print(28//3)

bool_var=False
print(type(bool_var))

elements = [2,3,"pi",5,7,11]
print(elements[2])
elements.append("mighty extension")
print(elements)
elements += ['jake', 'blake']
print(elements[3:8])
print(elements[3:])
print(elements[3:8:2])
print(elements[-1], elements [-3])
print(elements * 2)