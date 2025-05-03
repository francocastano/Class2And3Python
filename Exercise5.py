"""
Ejercicio 5

Ingrese un número entero y determine si es negativo, positivo o 0.
Escriba múltiples soluciones, que utilicen diferentes condiciones,
estructuras de control anidadas y no anidadas.
"""

number = int(input())


def sign_of_number(number:int) -> str:
    if number > 0:
        return "el numero es positivo"
    elif number < 0:
        return "el numero es negativo"
    else:
        return "el numero es 0"

def sign_of_number(number:int) -> str:
    if number > 0:
        message = "el numero es positivo"
    elif number < 0:
        message =  "el numero es negativo"
    else:
        message = "el numero es 0"
    return message

def sign_of_number(number:int) -> str:
    message = "el numero es 0"
    if number > 0:
        message = "el numero es positivo"
    if number < 0:
        message =  "el numero es negativo"
    return message

def sign_of_number(number:int) -> str:
    if number > 0:
        return "el numero es positivo"
    if number < 0:
        return "el numero es negativo"
    return"el numero es 0"

def sign_of_number(number:int) -> str:
    if number:
        if number > 0:
            return "el numero es positivo"
        if number < 0:
            return "el numero es negativo"
    return "el numero es 0"

print(sign_of_number(number))