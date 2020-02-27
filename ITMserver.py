import os

hostname="www.itmorelia.edu.mx"

respuesta=os.system("ping -c 1 "+hostname)

if respuesta==0:
    print(hostname + ": esta en funcionamiento")
else:
    print(hostname + ": no funciona")