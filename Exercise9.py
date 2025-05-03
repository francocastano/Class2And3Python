"""
Ejercicio 9

Reescriba las estructuras de control de manera que el programa sea equivalente, pero más legible.
"""
from random import randint

a = randint(1, 10); b = randint(1, 10); c = randint(1, 10)

print({ "a": a, "b": b, "c": c })

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)