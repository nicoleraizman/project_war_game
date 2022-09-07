from Player_ import Player
from Deck_of_cards import DeckOfCards


class CardGame:
    def __init__(self,name_p1, name_p2, num_cards=26):
        self.d = DeckOfCards()
        if num_cards > 26 or num_cards < 10:
            num_cards = 26
        self.name1 = name_p1
        self.name2 = name_p2
        self.num_cards = num_cards
        self.p1 = Player(self.name1,self.num_cards)
        self.p2 = Player(self.name2,self.num_cards)
        self.new_game()

    def new_game(self):
        self.d.cards_shuffle()
        for i in range(self.num_cards):
            self.p1.set_hand(self.d)
            self.p2.set_hand(self.d)


    def get_winner(self):
        if len(self.p1.stack_cards) > len(self.p2.stack_cards):
            return self.p1
        elif len(self.p1.stack_cards) == len(self.p2.stack_cards):
            return None
        else:
            return self.p2


