#Ejemplo 1 - Generador de contraseñas

import random

Letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(".....................Generador de contraseñas.....................")
    
cl = int(input('Ingrese la cantidad de letras: '))
cs = int(input('Ingrese la cantidad de simbolos: '))
cn = int(input('Ingrese la cantidad de números: '))

password = []

for i in range (1,cl+1):
    password.append(random.choice(Letras))
    
for i in range (1,cs+1):
    password.append(random.choice(Simbolos))

for i in range (1,cn+1):
    password.append(random.choice(Numeros))
    
random.shuffle(password)
clave = ""
for i in password:
    clave += i

print("La clave generada es: %s" %clave)