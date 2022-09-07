from Card import Card
from Deck_of_cards import DeckOfCards
from Player_ import Player
from CardGame import CardGame

name_p1 = input("enter the name of the first player: ")
name_p2 = input("enter the name of the second player: ")
num_cards = int(input("enter number of cards: "))
cardgame1 = CardGame(name_p1,name_p2,num_cards)
print(cardgame1)

name_p1 = Player(name_p1,num_cards)
name_p2 = Player(name_p2,num_cards)
for i in range(10):
    card_play1 = cardgame1.player1.get_card()
    card_play2 = cardgame1.player2.get_card()
    print(f"card player1 {card_play1} card player2 {card_play2}")
    if card_play1 > card_play2:
        cardgame1.player1.add_card(card_play2)
        cardgame1.player1.add_card(card_play1)
        print(f"winner is {cardgame1.player1.name}")
    else:
        cardgame1.player2.add_card(card_play1)
        cardgame1.player2.add_card(card_play2)
        print(f"winner is {cardgame1.player2.name}")

if cardgame1.get_winner()==None:
    print("no winner")
else:
    print(cardgame1.get_winner())







# p1 = Player(name_p1,num_cards)
# p2 = Player(name_p2,num_cards)
# p1.set_hand(deck_cards)
# p2.set_hand(deck_cards)






