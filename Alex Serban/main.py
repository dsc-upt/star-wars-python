print('Hello world!')

"""
Tipuri built-in:
- chr = char, caracter
- str = string, sir de caractere
- int = integer, intreg
- float = float, numere reale
- bool = boolean, True sau False
- list = ordered and indexed list
- tuple = ordered and indexed immutable list, lista nemodificabila
- set = unordered and unindexed list
- dict = dictionary, dictionar care contine perechi cheie - valoare
"""

cat = "AnaKin"
print(cat.lower())

#type = returneaza tipul variabilei
print (type(cat))

cat = 4
print(type(cat))

print(4 * 5)   # 20 -> inmultire
print(3 ** 4)   # 81 -> ridicare la putere
print(14 / 25)   # 0.56 -> impartire de nr reale
print(45 // 4)   # 11 -> impartire de intregi


def function ():
    print("Hey")
    lmao = "lmao"
    print(lmao)
# ce nu mai are tab nu intra in functie, aici functioneaza pe baza de indentare
function()