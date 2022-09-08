class Card:

    def __init__(self, suit, value):

        # Check type of suit
        if type(suit) != str:
            raise TypeError('invalid type of suit,must be str')
        # Check type of value
        if type(value) != int:
            raise TypeError('invalid type of value,must be int')
        # check that value is in range 1-13
        if value > 13 or value < 1:
            raise ValueError('invalid value,value must be between 1-13')
        # check that suit is only Dimond, Spade, Heart, or Club
        if suit != 'Diamond' and suit != 'Spade' and suit != 'Heart' and suit != 'Club':
            raise ValueError('invalid suit,suit must be Diamond or Spade or Heart or Club ')

        self.suit = suit
        self.cards_suit = {'Diamond':1, 'Spade':2, 'Heart':3, 'Club':4}
        # special occasions
        if value == 11:
            value = 'Jack'
        if value == 12:
            value = 'Queen'
        if value == 13:
            value = 'King'
        if value == 1:
            value = 'Ace'
        self.value = value
        self.cards_value = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

    def __repr__(self):
        return f"{self.suit}-{self.value}"

    """checking which value high then other and if they equal
        he checking which suit high then other."""
    def __gt__(self, other):
        if isinstance(other, Card):
            if self.cards_value[self.value] > other.cards_value[other.value]:
                return True
            elif self.cards_value[self.value] == other.cards_value[other.value]:
                if self.cards_suit[self.suit] > other.cards_suit[other.suit]:
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
            if self.cards_value[self.value] == self.cards_value[other.value] and self.cards_suit[self.suit] == self.cards_suit[other.suit]:
                return True
            else:
                return False
        else:
            raise TypeError('it must be class Card')

