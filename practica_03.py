# practica 3
# dada la lista mi_lista_2 = ["lunes", "martes", "miercoles","jueves","viernes"]
# imprimir cada elemento de la lista tres veces y cuando sea lunes no lo incluyas
# pista: usados dos tipos loops while y for en el mismo programa para hacerlo
# resultado:
# martes
# miercoles
# jueves
# viernes
# martes
# miercoles
# jueves
# viernes
# martes
# miercoles
# jueves
# viernes

mi_lista_2=  ["lunes", "martes", "miercoles","jueves","viernes"]

contador = 0
while contador < 3:
    for dia in mi_lista_2:
        if dia != "lunes":
            print(dia)
    contador += 1