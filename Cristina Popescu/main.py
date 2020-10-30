print('Hello world!')

"""
Tipuri built-in:
- chr = char, caracter
- str = string, siruri de caractere
- int = integer, intreg
- float = float, numere reale
- bool = boolean , True sau False
- list = ordered and indexed list
- tuple = ordered and indexed immutable list, lista nemodificabila
- set = unordered and unindexed list, nu se stie ce elemente ne pica 
- dict = dictionary, dictionar care contine perechi cheie - valoare

"""
cat = "Anakin"
print(cat[3])
print(cat.lower())

# type = returneaza tipul variabilei
print(type(cat))

cat = 4
print(cat)
print(type(cat))

print(4 * 5) # 20: inmultire
print(3 ** 4) # 81: ridicare la putere
print(14 / 23) # 0.6086956521739131: impartire de nr. reale -returneaza float
print(45 // 4) # 11: impartire fara rest - returneaza intregul


def function():
    abracadabra = "something"
    print('hello')
    print(abracadabra)


function()
