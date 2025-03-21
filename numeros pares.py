
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
while True:
    try:
        numero = int(input("Ingresa un número: "))
        break
    except ValueError:
        print("Por favor, ingresa un número válido.")
if es_par(numero):
    print("El número es par.",numero) 
else:
    print("El número es impar.",numero)
