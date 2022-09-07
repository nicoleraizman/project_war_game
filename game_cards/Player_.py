from Deck_of_cards import DeckOfCards
from Card import Card
import random

class Player:
    def __init__(self, name, num_cards=26):
        self.name = name
        self.num_cards = num_cards
        self.stack_cards = []

    def set_hand(self, d:DeckOfCards):
        d = DeckOfCards()
        for i in range(self.num_cards):
            random_card = d.deal_one()
            self.stack_cards.append(random_card)

    def get_card(self):
        card_from_stack = random.choice(self.stack_cards)
        self.stack_cards.remove(card_from_stack)
        return card_from_stack

    def add_card(self, c:Card):
        c = Card(value , suit)
        self.stack_cards.append(c)
