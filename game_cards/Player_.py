from Deck_of_cards import DeckOfCards
from Card import Card
import random

class Player:
    """this function creating a player"""
    def __init__(self, name, num_cards=26):
        self.name = name
        self.num_cards = num_cards
        self.stack_cards = []

    def __repr__(self):
        return f"{self.name}"
    """deal cards to players"""
    def set_hand(self, deck_of_cards:DeckOfCards):
        for i in range(self.num_cards):
            random_card = deck_of_cards.deal_one()
            self.stack_cards.append(random_card)

    """get a random card from the player stack"""
    def get_card(self):
        card_from_stack = random.choice(self.stack_cards)
        self.stack_cards.remove(card_from_stack)
        return card_from_stack
    """get a card and put the card in the player stack"""
    def add_card(self, card:Card):
        self.stack_cards.append(card)

