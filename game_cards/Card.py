class Card:

    def __init__(self, suit, value):
        # Check type of suit
        if type(suit) != int:
            raise TypeError('invalid type of suit,must be int')
        # Check type of value
        if type(value) != int:
            raise TypeError('invalid type of value,must be int')

        self.suit = suit

        self.value = value

    """checking which value high then other and if they equal
        he checking which suit high then other"""
    def __gt__(self, other):
        if isinstance(other, Card):
            if self.value > other.value:
                return True
            elif self.value == other.value:
                if self.suit > other.suit:
                    return True
                else:
                    return False
            else:
                return False
        else:
            raise TypeError('it must be ')

    """checking which if the value is equal"""
    def __eq__(self, other):
        if self.value == other:
            return True
        else:
            return False