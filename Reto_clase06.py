i=0
suma=0

while i < 30:
    i += 2
    if i < 10:
        continue
    suma += i
    print(i)
print(f"la suma es: {suma}")
