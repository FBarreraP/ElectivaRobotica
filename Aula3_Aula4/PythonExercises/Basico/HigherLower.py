from HiguerLowerArt import logo, vs
import HiguerLowerData as HLD
from random import randint
from replit import clear

def comparation(A, B):
    while A == B:
        B = randint(0,49)
    print(f"Compare A: {HLD.data[A]['name']}, a {HLD.data[A]["description"]}, from {HLD.data[A]['country']}")
    print(vs)
    print(f"Compare B: {HLD.data[B]['name']}, a {HLD.data[B]["description"]}, from {HLD.data[B]['country']}")

    if HLD.data[A]['follower_count'] > HLD.data[B]['follower_count']:
        winner = 'A'
        temp = A
    elif HLD.data[A]['follower_count'] < HLD.data[B]['follower_count']:
        winner = 'B'
        temp = B
    # else:
    #     winner = 'C'
    return winner, temp

def game():
    A = randint(0,49)
    B = randint(0,49)
    winner, temp = comparation(A, B)
    cont = 0
    next = True
    while next:
        choose = input("Quién tiene más seguidores?, digite 'A' ó 'B': ").upper()
        clear()
        if choose == winner:
            if winner == 'A':
                print(f"{HLD.data[A]['name']} tiene más seguidores que {HLD.data[B]['name']} ")
            elif winner == 'B':
                print(f"{HLD.data[B]['name']} tiene más seguidores que {HLD.data[A]['name']} ")
            cont += 1
            print(f'Muy bien, su puntaje es: {cont}')
            A = temp    
            B = randint(0,49)
            winner, temp = comparation(A, B)
        else:
            print('Perdió')
            next = False
        

print(logo)
    
game()