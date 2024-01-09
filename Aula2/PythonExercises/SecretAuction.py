from replit import clear
import SecretAuctionArt as SAA

def HighestBidder(BiddingRecord):
    HighestBid = 0
    winner = ""
    for bidder in BiddingRecord:
        BidAmount = BiddingRecord[bidder]
        if BidAmount > HighestBid:
            HighestBid = BidAmount
            winner = bidder
    print(f'El ganador es {winner} con una oferta de ${HighestBid}')

dictionary = {}

print(SAA.logo)

answer = 'sí'
while answer == 'si' or answer == 'sí':
    n = input('Ingrese su nombre: ')
    b = int(input('Ingrese su oferta: $'))
    dictionary[n] = b

    answer = input('Desea seguir ingresando otra oferta en la subasta, digite "sí" o "no"')
    clear()

print(f'diccionario: {dictionary}')
HighestBidder(dictionary)