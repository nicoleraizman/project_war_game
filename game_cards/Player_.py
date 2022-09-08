from Deck_of_cards import DeckOfCards
from Card import Card
import random

class Player:
    """this function creats a player."""
    def __init__(self, name:str, num_cards=26):
        if type(num_cards)!=int:
            raise TypeError("number of cards has to be of type int!!!")
        if num_cards > 26 or num_cards < 10:
            num_cards = 26
        self.name = name
        self.num_cards = num_cards
        self.stack_cards = []

    def __repr__(self):
        return f"{self.name}"

    """a function that gives the players cards from the stack, according to how many cards they need to get """
    def set_hand(self, deck_of_cards:DeckOfCards):
        for i in range(self.num_cards):
            random_card = deck_of_cards.deal_one()
            self.stack_cards.append(random_card)

    """get a random card from the player's stack"""
    def get_card(self):
        """makes sure that the stack of a player is not empty"""
        if len(self.stack_cards) == 0:
            raise ValueError("no more cards")

        card_from_stack = random.choice(self.stack_cards)
        self.stack_cards.remove(card_from_stack)
        return card_from_stack

    """get a card and put the card in the player stack"""
    def add_card(self, card:Card):
        self.stack_cards.append(card)


