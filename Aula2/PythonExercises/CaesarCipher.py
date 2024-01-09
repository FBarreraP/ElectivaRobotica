from CaesarArt import logo

print(logo)

Letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text,number,order):
    end_text = ""
    for char in text:
        if char in Letras:
            position = Letras.index(char)
            if order == 'codificar':
                new_position = position+number
                if new_position > 25:
                    new_position = new_position - 26
            else:
                new_position = position-number
            end_text += Letras[new_position]
        else:
            end_text += char
    print(f'El texto final de {order} es: {end_text}')

answer = 'sí'
while answer == 'sí' or answer == 'si': 

    task = input('Ingrese la tarea a realizar: "codificar" para encriptar o "descodificar" para descriptar: ')
    message = input('Ingrese la palabra: ').lower()
    shift = int(input('Ingrese el número de corrimientos: '))
    shift %= 26

    caesar(message,shift,task)
    answer = input('Desea correr el programa otra vez, digite "sí" o "no": ').lower()

print('chao')