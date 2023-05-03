def Calcular():
    print("-----------------------------")
    print("\n         Bienvenido\n")
    print("-----------------------------")
    print("Calculadora con menú simple\n")

num1=int(input("Ingrese el primero número:\n>"))
num2=int(input("Ingrese el segundo número:\n>"))
print("")

print("¿Qué operación desea realizar?\n")

def Menu():
    print("opciones:\n")
    print("-1=suma\n")
    print("-2=resta\n")
    print("-3=multiplicacion\n")
    print("-4=division\n")
Menu()
opcion=int(input("Ingrese su opcion\n>"))
print(" ")

while opcion != 0:
    if opcion == 1:
       result=num1+num2
       print("El resultado es: \n", result)
       quit()
    elif opcion == 2:
        result=num1-num2
        print("El resultado es: \n", result)
        quit()
    elif opcion == 3:
        result=num1*num2
        print("El resultado es: \n", result)
        quit()
    elif opcion == 4:
        result=num1/num2   
        print("El resultado es: \n", result)
        quit()
    else:
        print("elija una opcion valida")

        Menu()
        opcion=int(input("Ingrese su opcion\n>"))
        print(" ")

