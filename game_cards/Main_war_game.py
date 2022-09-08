from Player_ import Player
from CardGame import CardGame

name_p1 = input("enter the name of the first player: ")
name_p2 = input("enter the name of the second player: ")

num_cards = input("enter number of cards: ")
while not num_cards.isnumeric():
    print("please enter a number!!!")
    num_cards = input("enter number of cards: ")
num_cards = int(num_cards)

cardgame1 = CardGame(name_p1,name_p2,num_cards)
print(cardgame1)

name_p1 = Player(name_p1,num_cards)
name_p2 = Player(name_p2,num_cards)

for i in range(10):
    card_play1 = cardgame1.player1.get_card()
    card_play2 = cardgame1.player2.get_card()
    print(f"{cardgame1.name1}'s card: {card_play1} VS {cardgame1.name2}'s card: {card_play2}")
    if card_play1 > card_play2:
        cardgame1.player1.add_card(card_play2)
        cardgame1.player1.add_card(card_play1)
        print(f"The winner is {cardgame1.player1.name}!!!")
    else:
        cardgame1.player2.add_card(card_play1)
        cardgame1.player2.add_card(card_play2)
        print(f"The winner is {cardgame1.player2.name}!!!")

if cardgame1.get_winner() is None:
    print("It's a tie!")
else:
    print(f"The winner in the game is : {cardgame1.get_winner()}!")
