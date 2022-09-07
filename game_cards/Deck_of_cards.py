from Card import Card
import random

class DeckOfCards:
    """52 different cards are created here, and are all in one stack. the stack is of type list."""
    def __init__(self):
        list_cards = []
        suits = ["Diamond","Spade","Heart","Club"]
        for suit in suits:
            for value in range(1,14):
                c = Card(suit,value)
                list_cards.append(c)
        self.list_cards = list_cards

    """this function takes the stack and mixes it"""
    def cards_shuffle(self):
        random.shuffle(self.list_cards)

    """this function takes and removes a random card from the stack. It also returns the card."""
    def deal_one(self):
        if len(self.list_cards) == 0:
            raise ValueError("no more cards")

        random_card = random.choice(self.list_cards)
        self.list_cards.remove(random_card)
        return random_card

