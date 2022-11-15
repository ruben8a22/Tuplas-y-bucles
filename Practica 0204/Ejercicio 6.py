#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia
# y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las
# asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
aprobadas = []

for asignatura in asignaturas:
    resultado = float(input("¿Qué nota has sacado en " + asignatura + "?"))
    if resultado >= 5:
        aprobadas.append(asignatura)
for asignatura in aprobadas:
    asignaturas.remove(asignatura)
print("Tienes que repetir " + str(asignaturas))