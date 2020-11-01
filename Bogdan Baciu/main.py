paste = "spaghete"
print(paste)

paste =2
print(type(paste))

print(4 ** paste)
print(16 / 4)
print(16 // 3)


integer_var = int ('5') #conv din string in float
float_var = float("5.5") #conv din string in int
print(type(float_var))
print(type(integer_var))

bool_var = True
print(bool_var)
print(type(bool_var))

elems = [14, True, "spaghete"]
print(elems[2])
elems.insert(2,"whooo")
print(elems)

elems = elems + ['DAMI MANCARE']
print(elems[:2])#de la 0 la 2
print(elems[2:])#de la 2 la final
print(elems[1:6:2])
print(elems[-3])