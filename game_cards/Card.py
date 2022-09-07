class Card:

    def __init__(self, suit, value):
        # Check type of suit
        if type(suit) != str:
            raise TypeError('invalid type of suit,must be str')
        # Check type of value
        if type(value) != int or str:
            raise TypeError('invalid type of value,must be int or str')

        self.suit = suit
        self.cards_suit = {'Diamond':1, 'Spade':2, 'Heard':3, 'Club':4}

        self.value = value
        self.cards_value = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

    """checking which value high then other and if they equal
        he checking which suit high then other"""
    def __gt__(self, other):
        if isinstance(other, Card):
            if self.cards_value[self.value] > other.cards_value[self.value]:
                return True
            elif self.cards_value[self.value] == other.cards_value[self.value]:
                if self.cards_suit[self.suit] > other.cards_suit[self.suit]:
                    return True
                else:
                    return False
            else:
                return False
        else:
            raise TypeError('it must be class Card')

    """checking which if the value is equal"""
    def __eq__(self, other):
        if isinstance(other, Card):
            if self.cards_value[self.value] == other.cards_value[self.value]:
                return True
            else:
                return False
        else:
            raise TypeError('it must be class Card')
