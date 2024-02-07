from BlackJackArt import *
import random
from replit import clear

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2: #21 con BlackJack (AS+10)
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Usted perdió, el oponente tiene BlackJack"
    elif user_score == 0:
        return "Usted gana con un BlackJack"
    elif user_score > 21:
        return "Usted se pasó, usted perdió"
    elif computer_score > 21:
        return "El oponente se pasó, usted ganó"
    elif user_score > computer_score:
        return "Usted ganó"
    else:
        return "Usted perdió"
    
def play_game():
    print(logo)
    
    user_cards = []
    computer_cards = []
    game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over: #Turno del usuario
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f'Sus cartas {user_cards}, su puntaje {user_score}')
        print(f'La primera carta del computador {computer_cards[0]}')

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_deal = input("Desea otra carta?, digite 'sí' o 'no': ")
            if user_deal == 'sí' or user_deal == 'si':
                user_cards.append(deal_card())
            else: 
                game_over = True

    while computer_score != 0 and computer_score < 17: #Turno del computador
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f'Su mano final {user_cards}, su puntaje {user_score}')
    print(f'La mano final del computador {computer_cards}, su puntaje {computer_score}')
    print(compare(user_score, computer_score))
    
answer = 'sí'

while answer == 'sí' or answer == 'si':
    clear()
    play_game()
    answer = input("Desea jugar BlackJack?, digite 'sí' o 'no':")
