from NumberGuessArt import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def dificulty():
    level = input('Digite el modo a jugar, fácil o difícil: ')
    if level == 'fácil':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def check_answer(number_guess, number_random, turns):
    if number_guess > number_random:
        print(f'el número {number_guess} es muy alto\n')
        return turns - 1
    elif number_guess < number_random:
        print(f'el número {number_guess} es muy bajo\n')
        return turns - 1
    else:
        print(f'Adivinó el número {number_random}')
        

def game():
    print(logo)
    number_random = random.randint(0,100)
    print(f'La respuesta es {number_random}')
    print('Adivine el número de 0 a 100')
    turns = dificulty()
    print(f"Tiene {turns} intentos para adivinar el número \n")
    number_guess = 101
    while number_guess != number_random:
        print(f'.......Intento {turns}.......')
        number_guess = int(input("Digite el número: "))
        turns = check_answer(number_guess, number_random, turns)

        if turns == 0:
            print(f'Perdió, era el número {number_random}')
            break
        
game()