Nombre = str(input("Ingrese su Nombre :"))
Genero = str(input("Ingrese su Género :"))
Genero_1 = Genero [0]
Nombre_1 = Nombre[0]

if Genero_1 == "M" and Nombre_1 < "M" or Genero_1 == "H" and Nombre_1 > "N":
    print("Grupo A")
else:
    print("Grupo B")
    
    
