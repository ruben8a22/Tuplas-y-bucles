# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene
# en una lista y los muestre por pantalla ordenados de menor a mayor.

numeros = []
for n in range(6):
    numeros.append(int(input("Introduce el numero ganador:")))
    numeros.sort()
    print("Los numeros ganadores son", str(numeros))