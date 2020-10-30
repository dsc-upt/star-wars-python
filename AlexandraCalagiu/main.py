print('May the Force be with you!')

"""
Tipuri built-in:
    -chr = char, caracter
    -str = string, siruri de caractere
    -int = integer, nr intregi
    -float = float, nr reale
    -bool = boolean, True sau False
    -list = ordered and indexed list
    -tuple = ordered and indexed immutable list, lista nemodificabila
    -set = unordered and unindexed list
    -dict = dictionary containing key-value pairs
"""
cat = "Anakin"
print(cat)
print(type(cat))

# type returneaza tipul variabilei

cat = 3
print(cat)
print(type(cat))
print(4 * 5) # 20
print(3 ** 4) # 81 ; pow
print(14 / 23) # 0.6086956521739131
print(45 // 4) # 11

def function():
    abracadabra = "something"
    print(abracadabra)

function()

integer_val = int('5')  # convert string to int
float_var = float('6.8')  # convert string to float
print(type(integer_val))
print(type(float_var))

bool_var = True
print(bool_var)
print(type(bool_var))

#           0  1  2   3       4     5    -indexes
elements = [3, 5, 7, True, "Luke", 5.9]  # lists are mutable
#            -6 -5 -4  -3     -2     -1
print(elements)
print(elements[4])
elements.append('New item')  # add new item
print()
print(elements)
# elements.insert(4, "Leia")
elements = elements + ['Added item']
elements += ['Leia']

print(elements)
print(elements[2:6])  # ret substring from pos 2 to 6 (without the on pos 6)
print(elements[:4])  # ret substring from start to pos 4 (without the on pos 4)
print(elements[2:])  # ret substring from pos 2 to the end
print(elements[3:10:3])  # ret substring from pos 3 to 10 with pace 3 (without the on pos 10)

print(elements[-5 :-2])
print(elements[-2:-5:-1])
print(elements[5:2:-1])
print(elements * 3)  # it prints the list 3 times