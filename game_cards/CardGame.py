from Player_ import Player
from Deck_of_cards import DeckOfCards


class CardGame:
    """start a game."""
    def __init__(self,name_player1, name_player2, num_cards=26):
        self.d = DeckOfCards()
        if num_cards > 26 or num_cards < 10:
            num_cards = 26
        self.name1 = name_player1
        self.name2 = name_player2
        self.num_cards = num_cards
        self.player1 = Player(self.name1,self.num_cards)
        self.player2 = Player(self.name2,self.num_cards)
        self.new_game()

    """rebooting the game"""
    def new_game(self):
        self.d.cards_shuffle()
        self.player1.set_hand(self.d)
        self.player2.set_hand(self.d)

    """find the winner """
    def get_winner(self):
        if len(self.player1.stack_cards) > len(self.player2.stack_cards):
            return self.player1
        elif len(self.player1.stack_cards) == len(self.player2.stack_cards):
            return None
        else:
            return self.player2


