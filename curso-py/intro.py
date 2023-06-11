"""Introduccion a Python"""

print("Hola mundo!")
print("El weta " * 4)


def print_nums(x):
    for i in range(x):
        print(i)
        return


print_nums(10)


def func(x):
    res = 0
    for i in range(x):
        res += i
    return res


print(func(3))


# Entrar un texto y una palabra para ejecutar funcion search
text = input()
word = input()

"""
Funcion para buscar una palabra dentor de un texto cualquiera 
"""


def search(x, y):
    if y in x:
        print("Word found")
    else:
        print("Word not found")


x = text
y = word
# No se puede poner un print a la hora de llamar la funcion, te devuelve un 'None'
search(x, y)
