Renta_Anual = int(input("Ingrese su Renta Anual :"))

if Renta_Anual < 10000:
    
    print(f'Tienes que pagar el 5% de interes, que es : $ {"{:.2f}".format(Renta_Anual*0.05)}')
  
elif Renta_Anual >= 10000 and Renta_Anual <= 20000:
    
    print(f'Tienes que pagar el 15% de interes, que es : $ {"{:.2f}".format(Renta_Anual*0.15)}')

elif Renta_Anual > 20000 and Renta_Anual <= 35000:
    
    print(f'Tienes que pagar el 20% de interes, que es : $ {"{:.2f}".format(Renta_Anual*0.2)}')

elif Renta_Anual > 35000 and Renta_Anual <= 60000:
    
    print(f'Tienes que pagar el 30% de interes, que es : $ {"{:.2f}".format(Renta_Anual*0.3)}')

elif Renta_Anual > 60000:
    
    print(f'Tienes que pagar el 45% de interes, que es : $ {"{:.2f}".format(Renta_Anual*0.45)}')

print("Revisar la Renta")


