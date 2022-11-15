#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.



palabra = input("Introduce una palabra: ")
vocal = ["a","e","i","o","u"]
for n in palabra:
    if n in vocal:
        print("La vocal a aparece",palabra.count("a"), "veces")
        print("La vocal e aparece",palabra.count("e"), "veces")
        print("La vocal i aparece",palabra.count("i"), "veces")
        print("La vocal o aparece",palabra.count("o"), "veces")
        print("La vocal u aparece",palabra.count("u"), "veces")
        break