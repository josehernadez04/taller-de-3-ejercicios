def celsius_a_fahrenheit():
    celsius=float(input(" ingrese la temperatura "))
    return (celsius*1.8)+32
def fahrenheit_a_celsius():
    fahrenheit=float(input(" ingrese la temperatura "))
    return(fahrenheit-32)/1.8
while True:
    print(" esto es un convertidor de temperaturas ")
    print(" este son las dos opciones a elegir ")
    print(" 1. para Celsius a Fahrenheit")
    print(" 2. Fahrenheit a Celsius ")
    opcion=int(input(" ingrese el numero para hacer la convercion "))
    if opcion==1:
        print(" la conversion de Celsius a Fahrenheit es: ",celsius_a_fahrenheit())
    elif opcion==2:
        print("la conversion de Fahrenheit a Celsius es: ",fahrenheit_a_celsius())
        break
    else:
        print(" opcion erranea")