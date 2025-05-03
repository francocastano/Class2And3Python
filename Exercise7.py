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

def estacionamiento(seccion:str,hora:int) -> str | None:
    if seccion.lower() == "a":
        if hora == 1:
            return "$100"
        if hora == 2:
            return "$150"
        return "$200"
    if seccion.lower() == "b":
        if hora == 1:
            return "$80"
        if hora == 2:
            return "$120"
        return "$160"
    if seccion.lower() == "c":
        if hora == 1:
            return "$60"
        if hora == 2:
            return "$90"
        return "$120"

print(estacionamiento("A",2))