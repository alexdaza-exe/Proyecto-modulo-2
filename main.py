print("---Bienvenido al conversor de moneda---")
name=input("Nombre:")
print(" Ingrese la moneda a convertir ")
print(" 1. Peso mxn --> Dolar US ")
op=int(input(" 2. Dolar US --> Peso "))
match op:
    case 1:
        pesos=float(input("ingrese la cantidad de dinero en pesos MXN. que posee (valor actual del dólar: 17.50 Pesos MXN.)"))
        dolar=pesos/17.50
        print(f"Hola, {name} sus Pesos MXN: ${pesos} corresponden a ${dolar:.2f} USD. ")
    case 2:

        dolar=float(input("ingrese la cantidad de dinero en dolar US. que posee (valor actual del dólar: 17.50 Pesos MXN.)"))
        pesos=dolar*17.50
        print(f"Hola, {name} sus dolares US: ${dolar} corresponden a ${pesos:.2f} MXN. ")
    case _:
        print("opcion inválida")