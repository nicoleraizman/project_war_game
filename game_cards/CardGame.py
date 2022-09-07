from Player_ import Player

class CardGame:
    def __init__(self, name, num_cards=26):
        if num_cards > 26 or num_cards < 10:
            num_cards = 26
        self.name = name
        self.num_cards = num_cards

    def new_game(self,):
        p = Player(self.name,self.num_cards)
        for i in range(self.num_cards):
            p.set_hand()

        pass

    def get_winner(self):
        pass
