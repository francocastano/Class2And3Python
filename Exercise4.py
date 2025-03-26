"""
Ejercicio 4

Escriba una expresión para acceder a cada número que vea.
El resultado de imprimir las 4 en suceción debería ser 1, 2, 3, 4.
"""
elements = [
    1,
    {
        "two":2,
        "listthree":[3]
    },
    [[4]]
]

print(elements[0],elements[1]["two"],elements[1]["listthree"][0],elements[2][0][0])