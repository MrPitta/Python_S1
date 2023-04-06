print("\n         Bienvenido\n")
print("Calculadora con menú simple\n")

num1=int(input("Ingrese el primero número:\n>"))
num2=int(input("Ingrese el segundo número:\n>"))
print("")

print("¿Qué operación desea realizar?\n")

def Menu():
    print("opciones: 1=suma | 2=resta | 3=multiplicación | 4=division \n")

Menu()
opcion=int(input("Ingrese su opcion\n>"))

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