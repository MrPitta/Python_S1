s=00
m=00
h=00

while h < 24:
    while m < 60:
        while s < 60:
            s += 1
            print(f"{h}:{m}:{s}")
        s = 0    
        m += 1
    m = 0
    h += 1