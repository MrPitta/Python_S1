tempminimas= (9,5,2,7,6,1)
tempmaximas= (12,14,11,10,15,9)

print(tempminimas)
print(tempmaximas)

if 9 in tempminimas and 9 in tempmaximas:
    print("A) La temperatura 9°C se encuentra en ambos sets.\n")
else:
    print("A) La temperatura 9°C no se encuentra en ambos sets.\n")

if 6 and 17 in tempminimas or 6 and 17 in tempmaximas:
    print("B) La temperatura 6°C y 17°C si se encuentra en al menos un set.\n")
else:
    print("B) La temperatura 6°C y 17°C si se encuentra en al menos un set.\n")

tempminimas= (9**4,5**4,2**4,7**4,6**4,1**4)
tempmaximas= (12**4,14**4,11**4,10**4,15**4,9**4)
print(f"C) {tempminimas}")
print(f"C) {tempmaximas}")
temptodas= (tempminimas,tempmaximas)
print(temptodas)