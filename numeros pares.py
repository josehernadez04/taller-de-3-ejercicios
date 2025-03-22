def tomar_datos():
    numero=int(input(" regalame un numero "))
    return numero 
    
def procedimiento(numero):
    return numero % 2 == 0

def resultado(numero):
    if procedimiento(numero):
        print(" el numero es par ")
    else:
        print(" el numero es impar ")
def menu():
    print(" 1. para saber si el numero es par o impar ")
    print(" 2. para salir ")
    opc=int(input(" digites el numero "))
    return opc
while True:
    opcion=menu()
    if opcion ==1:
        numero=tomar_datos()
        resultado(numero)
    elif opcion==2:
        print(" hasta luego ")
    else:
        print(" opcion incorrecta ")       