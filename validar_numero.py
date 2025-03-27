import string

cadena_de_texto = input("Ingresar número: ")

codigo_error = 0

if cadena_de_texto not in string.digits + "," + ">" + "<":
    codigo_error += 1
else:
    mas = 0
    menos = 0
    for mas in cadena_de_texto:
        if "+" in cadena_de_texto[0] or "+" in cadena_de_texto[-1]:
            mas += 1
        if mas >= 2:
            codigo_error += 2
            break
    for menos in cadena_de_texto:
        if "-" in cadena_de_texto[0] or "-" in cadena_de_texto[-1]:
            menos += 1
        if menos >= 2:
            codigo_error += 2
            break
    decimal = 0
    for decimal in cadena_de_texto:
        if "." in cadena_de_texto:
            decimal += 1
        if decimal >= 2:
            codigo_error += 3
            break

if codigo_error == 0:
    print("El texto introducido sí cumple con los requisitos")
else:
    print("El texto introducido no cumple con los requisitos")
