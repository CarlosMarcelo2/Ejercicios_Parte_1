pizza_vegetariana = "Ingridientes: Pimiento, Tofu"
pizza_no_vegetariana = "Ingredientes: Peperoni, Jamón y Salmón"

tipo_pizza = input("¿Quieres una pizza vegetariana, o no?. Ingresa 'Si' o 'No': ")


if tipo_pizza == "si":
    print(pizza_vegetariana)
    Ingrediente = str(input("¿Elije un ingrediente: "))
    print(f'La pizza elegida es vegetariana y los ingredientes son: {Ingrediente}, tomate y mozarella')

else:
    print(pizza_no_vegetariana)
    Ingrediente = str(input("¿Elije un ingrediente: "))
    print(f'La pizza elegida no es novegetariana y los ingredientes son: {Ingrediente}, tomate y mozarella')






