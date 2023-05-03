ciudades = ["Santiago","Temuco","Osorno","Punta Arenas"] 
ica = [134,99,245,50]

ica_min = min(ica)
ica_max = max(ica)
ciudad_ica_min = ica.index(ica_min)
ciudad_ica_max = ica.index(ica_max)

print(f"La ciudad con el ICA más bajo es: {ciudades[ciudad_ica_min]}")
print(f"La ciudad con el ICA más alto es: {ciudades[ciudad_ica_max]}")

for i in range(len(ciudades)):
    if ica[i] >= 0 and ica[i]<= 50:
        print(ciudades[i],"tiene un indice de calidad del aire BUENO")
    elif ica[i] >= 51 and ica[i]<= 100:
        print(ciudades[i],"Tiene un indice de calidad del aire MODERADO")
    elif ica[i] >= 101 and ica[i]<= 150:
        print(ciudades[i],"Tiene un indice de calidad del aire DAÑINA A LA SALUD PARA GRUPOS SENSIBLES")
    elif ica[i] >= 151 and ica[i]<= 200:
        print(ciudades[i],"Tiene un indice de calidad del aire DAÑINA A LA SALUD")
    elif ica[i] >= 201 and ica[i]<= 300:
        print(ciudades[i],"Tiene un indice de calidad del aire MUY DAÑINA A LA SALUD")    
    elif ica[i] > 300:
        print(ciudades[i],"Tiene un indice de calidad del aire PELIGROSO")