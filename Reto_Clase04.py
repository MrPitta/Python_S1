print("---Paciente uno---")

nombre1=input("Ingrese el nombre:\n>")
peso1=float(input("Ingrese el peso:\n>"))
estatura1=int(input("Ingrese la estatura:\n>"))
edad1=int(input("Ingrese la edad:\n>"))

while edad1 < 1 or edad1 >130:
    print("Ingrese una edad valida...")
    edad1=int(input("Ingrese la edad:\n>"))
#--------------------------------------------------#
print("---Paciente dos---")

nombre2=input("Ingrese el nombre:\n>")
peso2=float(input("Ingrese el peso:\n>"))
estatura2=int(input("Ingrese la estatura:\n>"))
edad2=int(input("Ingrese la edad:\n>"))

while edad2 < 1 or edad1 >130:
    print("Ingrese una edad valida...")
    edad1=int(input("Ingrese la edad:\n>"))
#--------------------------------------------------#
print("---Paciente tres---")

nombre3=input("Ingrese el nombre:\n>")
peso3=float(input("Ingrese el peso:\n>"))
estatura3=int(input("Ingrese la estatura:\n>"))
edad3=int(input("Ingrese la edad:\n>"))

while edad3 < 1 or edad1 >130:
    print("Ingrese una edad valida...")
    edad1=int(input("Ingrese la edad:\n>"))

paciente1=(nombre1,peso1,estatura1,edad1)
paciente2=(nombre2,peso2,estatura2,edad2)
paciente3=(nombre3,peso3,estatura3,edad3)

lista=[paciente1,paciente2,paciente3]

print(lista)