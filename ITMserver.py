import os

hostname="www.itmorelia.edu.mx"

respuesta=os.system("ping -c 1 "+hostname)

if respuesta==0:
    print(hostname + ": esta en funcionamiento")
else:
    print(hostname + ": no funciona")

comp="200.33.171.0/24"

os.system("nmap -sP "+comp)