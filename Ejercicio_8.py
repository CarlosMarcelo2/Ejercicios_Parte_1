var_interes = 0.04
monto_inicial = int(input("Ingrese Monto Inicial :"))
saldo_año1 = monto_inicial + monto_inicial * var_interes
saldo_año2 = saldo_año1 + saldo_año1 * var_interes
saldo_año3 = saldo_año2 + saldo_año2 * var_interes
print("{:.2f}".format(saldo_año1))
print("{:.2f}".format(saldo_año2))
print("{:.2f}".format(saldo_año3))
