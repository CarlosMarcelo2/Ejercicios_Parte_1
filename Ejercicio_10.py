numerador = int(input("Ingrese numerador :"))
denominador = int(input("Ingrese denominador :"))

if denominador == 0:
    print("Error: No es posible dividir por 0")
else:
    resultado = numerador / denominador
    print("{:.2f}".format(resultado))
