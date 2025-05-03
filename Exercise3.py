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

print("Escriba un oracion")
phase = input()
print("Escriba una palabra")
word = input()

    # list_words = phase.split()
    # # phase_split = phase.split()
    # # index_word = phase_split.index(word)
    # if (word in list_words):
    #     print(list_words.index(word))
    # else:
    #     print("esta palabra no esta en la lista")

persona1 = {'dni':'12345678','nombre':'fernando'}
persona2 = {'dni':'12345679','nombre':'kevin'}
persona3 = {'dni':'12345677','nombre':'lorenzo'}

def is_included(phase:str,word:str) -> int | str:
    if word in phase:
        return phase.split().index(word)
    return "esta palabra no esta en la lista"

    
print(is_included(phase,word))