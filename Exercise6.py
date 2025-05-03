"""
Ejercicio 6

Dados 2 emails, verificar las siguientes condiciones:

1. El primer email es @austral.edu.ar
2. Los emails son iguales, salvo por mayúsculas y minúsculas. Ayuda: use el método `lower` o `upper`.

Si la condición 1 no se cumple, muestre un mensaje de error indicando el tipo de error.
Si la condición 2 no se cumple, muestre otro mensaje de error indicándolo.
Si ambas condiciones se cumplen, muestre que la verificación fue exitosa.
"""

mail1:str = "juanCiTo88@austral.edu.ar"
mail2:str = "juAnCiTo88@hotmail.com.ar"

austral = "@austral.edu.ar"

if austral not in mail1.lower():
    print("el mail no es austral")
elif mail1.lower() != mail2.lower():
    print("los emails no son iguales")
else: 
    print("la verificacion fue exitosa")

def is_austral(mail1:str,mail2:str) -> str:
    austral = "@austral.edu.ar"
    if austral not in mail1.lower():
        return "el mail no es austral"
    if mail1.lower() != mail2.lower():
        return "los emails no son iguales"
    return "la verificacion fue exitosa"
print(is_austral(mail1,mail2))

