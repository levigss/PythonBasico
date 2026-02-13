 #Loops

mi_lista = [1,2,3,4,5]

for i in mi_lista:
    print("El numero es:", i)

resultado = 0 
for i in mi_lista:
    resultado += i

print(f"El resultado de la suma de mi lista es: {resultado}")

for i in range(2, 9):
    print(i)

    mi_lista_2 = ["Lunes" , "Martes", "Miercoles", "Jueves", "Viernes"]

for i in mi_lista_2:
    if i != "Lunes":
            print(f"Feliz{i}!")