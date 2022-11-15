#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

palabra = input("Escribe una palabra:")
palabraAlReves = palabra
palabra = list(palabra)
palabraAlReves = list(palabraAlReves)
palabraAlReves.reverse()

if palabra == palabraAlReves:
    print("Es un palindromo")
else:
    print("No es un palindromo")