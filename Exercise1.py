"""
Ejercicio 1

Mostrar por pantalla la suma y el producto
de los dos números ingresados por el usuario.
"""

number1 = float(input())
number2 = float(input())


def plus(number1:float,number2:float) -> float:
    result = number1  + number2
    return result

def product (number1:float,number2:float) -> float:
    result = number1  * number2
    return result

print(plus(number1,number2))
print(product(number1,number2))
