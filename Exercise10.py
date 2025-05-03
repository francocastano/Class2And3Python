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

print(f'hola soy {filas[0]["nombre"]} y tengo {filas[0]["edad"]} y me gustan los {filas[0]["gustos"]}')
print(f'hola soy {filas[1]["nombre"]} y tengo {filas[1]["edad"]} y me gustan los {filas[1]["gustos"]}')
print(f'hola soy {filas[2]["nombre"]} y tengo {filas[2]["edad"]} y me gustan {filas[2]["gustos"]} animales')

def presentacion() -> str| None:
    