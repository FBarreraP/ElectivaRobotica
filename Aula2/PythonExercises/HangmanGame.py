#Ejemplo 2 - Juego del ahorcado

import random
from HangmanArt import *
from HangmanWords import word

display = []
end = False
lives = 6

chosen = random.choice(word)
length = len(chosen)

for i in range(0,length):
    display.append('_')

print(f'{logo} \n')

while end == False:
    guess = input('Adivine una letra: ').lower()

    for i in range (0,length):
        if guess == chosen[i]:
            print(f'Ha adivinado la letra: {guess}')
            display[i] = guess
    a = " ".join(display)
    print(f'Solución: {a}')
    
    if guess not in chosen:    
        lives -= 1 
        if lives == 0:
            print('perdió')
            end = True
        
                
    if '_' not in display:
        print('ganó')
        end = True 
    
    print(stages[lives])