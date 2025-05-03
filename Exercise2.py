"""
Ejercicio 2

Dada la siguiente lista, aplicar las siguientes transformaciones en orden:

1. Agregar el número 4 al final de la lista.
2. Agregar el número 0 al inicio de la lista.
3. Agregar el número 1 en la posición 3.
4. Eliminar el número 3 de la lista.
5. Imprimir la lista resultante.
"""

numbers: list[int | list[int]] = [2, 3, 5, 7, 11]

"""
Opcional

Observe que agregar la lista [1] a `numbers`
es posible, a pesar del tipo documentado de `numbers`,
pero no es lo mismo que agregar el número 1.
"""

def tranformations():
    numbers.append(4)
    print(numbers)
    numbers.insert(0,0)
    print(numbers)
    numbers.insert(3,1)
    print(numbers)
    print(numbers.pop(numbers.index(3)))
    print(numbers)
    numbers.append([1])
    print(numbers)
    return numbers
print(tranformations())