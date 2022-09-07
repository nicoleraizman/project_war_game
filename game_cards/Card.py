class Card:

    def __init__(self, suit, value):

        # Check type of suit
        if type(suit) != str:
            raise TypeError('invalid type of suit,must be str')
        # Check type of value
        if type(value) != int and type(value) != str:
            raise TypeError('invalid type of value,must be int or str')

        self.suit = suit
        self.cards_suit = {'Diamond':1, 'Spade':2, 'Heart':3, 'Club':4}

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




# c = Card('Diamond',11)
# print(c.cards_value['Jack'])
# print(c.cards_suit['Diamond'])
# c1 = Card('Spade',11)
# print(c1.cards_suit['Spade'])
# print(c1.cards_value['Jack'])
# if c1 > c:
#     print('eee')
# else:
#     print('ttt')
