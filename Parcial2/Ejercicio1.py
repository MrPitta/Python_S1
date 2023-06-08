palabra=input("Ingrese una palabra: ").lower()
palabrainvertida = palabra[::-1]

if palabra == palabrainvertida:
    print("La palabra es un palindromo")
else:
    print("La palabra no es un palindromo")