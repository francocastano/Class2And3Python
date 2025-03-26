"""
LECTURA COMPLEMENTARIA

Explicación sobre el uso de input()
https://www.w3schools.com/python/ref_func_input.asp

Documentar los tipos que las variables deberían contener (opcional, buena práctica)
https://docs.python.org/3/library/typing.html

Conversión de tipos de datos
https://www.geeksforgeeks.org/type-conversion-in-python
"""

number1: str   =       input("Ingrese un número, y luego presione ENTER: ")
number2: float = float(input("Ingrese otro número, y luego presione ENTER: "))

"""
Ejercicio 1

Mostrar por pantalla la suma y el producto
de los dos números ingresados por el usuario.
"""

"""
Ejercicio 2

Dada la siguiente lista, aplicar las siguientes transformaciones en orden:

1. Agregar el número 4 al final de la lista.
2. Agregar el número 0 al inicio de la lista.
3. Agregar el número 1 en la posición 3.
4. Eliminar el número 3 de la lista.
5. Imprimir la lista resultante.
"""

numbers: list[int] = [2, 3, 5, 7, 11]

"""
Opcional

Observe que agregar la lista [1] a `numbers`
es posible, a pesar del tipo documentado de `numbers`,
pero no es lo mismo que agregar el número 1.
"""

"""
Ejercicio 3

Pida al usuario que escria una oración, y luego pídale una palabra.
Determine en qué posición de la oración está la palabra, asumiendo que siempre existe.

Ayuda: use el método `split` para dividir una oración en una lista de palabras.

Opcional: si la palabra no está en la oración, muestre un mensaje de error.
"""

"""
Ingrese datos personales (nombre, dni) 3 veces y almacénelos en un diccionario.
Determine si algún DNI fue ingresado duplicado. Imprimir todos los DNIs y todos los nombres.
"""

people: dict[str, int] = {}

"""
Ejercicio 4

Escriba una expresión para acceder a cada número que vea.
El resultado de imprimir las 4 en suceción debería ser 1, 2, 3, 4.
"""

elements = [
    1,
    {
        "two": 2,
        "listthree": [3]
    },
    [[4]]
]

"""
Ejercicio 5

Ingrese un número entero y determine si es negativo, positivo o 0.
Escriba múltiples soluciones, que utilicen diferentes condiciones,
estructuras de control anidadas y no anidadas.
"""

"""
Ejercicio 6

Dados 2 emails, verificar las siguientes condiciones:

1. El primer email es @austral.edu.ar
2. Los emails son iguales, salvo por mayúsculas y minúsculas. Ayuda: use el método `lower` o `upper`.

Si la condición 1 no se cumple, muestre un mensaje de error indicando el tipo de error.
Si la condición 2 no se cumple, muestre otro mensaje de error indicándolo.
Si ambas condiciones se cumplen, muestre que la verificación fue exitosa.
"""

"""
Ejercicio 7

Tenemos la siguiente tabla de precios para un estacionamiento:

Sección A:
- 1 hora: $100
- 2 horas: $150
- 3 horas: $200

Sección B:
- 1 hora: $80
- 2 horas: $120
- 3 horas: $160

Sección C:
- 1 hora: $60
- 2 horas: $90
- 3 horas: $120

Dada una letra simbolizando la sección y un número simbolizando la cantidad de horas,
determine el precio a pagar, utilizando exclusivamente estructuras de control.
"""

"""
Ejercicio 8

Repita el ejercicio anterior, pero esta vez no usando ninguna estructura de control.
"""

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

"""
Ejercicio 10

Tenemos 3 registros de personas en nuestra base de datos,
cada uno con los siguientes campos:

- Nombre
- Edad
- Le gustan los perros, gatos, ambos, ninguno

Imprima los 3 registros de forma amigable para el usuario.
"""

filas: list[dict[str, int | str]] = [
    { "nombre": "Juan",  "edad": 20, "gustos": "perros" },
    { "nombre": "Ana",   "edad": 30, "gustos": "gatos" },
    { "nombre": "Pedro", "edad": 25, "gustos": "ambos" },
]


#Elabore un script en python que solicite al usuario el ingreso de 2 numeros(que
#pueden contener decimales). Sume ambos numeros y muestre por consola el
#resultado como entero, y mostrar si los numeros ingresados eran ambos
#enteros,ambos decimales,o uno y uno