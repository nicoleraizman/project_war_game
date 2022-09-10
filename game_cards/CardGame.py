from Player_ import Player
from Deck_of_cards import DeckOfCards


class CardGame:
    """start a game"""
    def __init__(self,name_player1, name_player2, num_cards=26):
        self.dack_of_card = DeckOfCards()
        if type(num_cards) != int:
            raise TypeError('num_cards must be int')
        if num_cards > 26 or num_cards < 10:
            num_cards = 26
        self.name1 = name_player1
        self.name2 = name_player2
        self.num_cards = num_cards
        self.player1 = Player(self.name1,self.num_cards)
        self.player2 = Player(self.name2,self.num_cards)
        """a part that helps the function new_game to be called *only* from the constructor"""
        self.new_game_is_work = False
        self.new_game()
        self.new_game_is_work = True

    """rebooting the game"""
    def new_game(self):
        # checks that the function new_game works only in init
        if self.new_game_is_work:
            raise Exception('new_game can use only in init')
        self.dack_of_card.cards_shuffle()
        self.player1.set_hand(self.dack_of_card)
        self.player2.set_hand(self.dack_of_card)

    """find the winner """
    def get_winner(self):
        if len(self.player1.stack_cards) > len(self.player2.stack_cards):
            return self.player1
        elif len(self.player1.stack_cards) == len(self.player2.stack_cards):
            return None
        else:
            return self.player2

    def __str__(self):
        return f" stack cards of player1: {self.player1.stack_cards} stack cards of player2:{self.player2.stack_cards} "