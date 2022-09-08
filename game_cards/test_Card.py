from unittest import TestCase
from Card import Card


class TestCard(TestCase):

    def setUp(self):
        self.card = Card('Club', 7)

# checks for valid values
    def test_init_valid_1(self):
        card = Card('Diamond', 5)
        self.assertEqual(card.value, 5)
        self.assertEqual(card.suit, 'Diamond')
        self.assertEqual(card.cards_value[5], 5)
        self.assertEqual(card.cards_suit['Diamond'], 1)

# checks valid values with an emphasis on numbers above 10
    def test_init_valid_2(self):
        card = Card('Diamond', 12)
        self.assertEqual(card.value, 'Queen')
        self.assertEqual(card.cards_value['Queen'], 12)

# checks legal borderline values
    def test_init_valid_3(self):
        card_1 = Card('Diamond', 13)
        card_2 = Card('Diamond', 1)
        self.assertEqual(card_1.value, 'King')
        self.assertEqual(card_1.cards_value['King'], 13)
        self.assertEqual(card_2.value, 'Ace')
        self.assertEqual(card_2.cards_value['Ace'], 14)

# checks for invalid values
    def test_init_invalid_1(self):
        with self.assertRaises(TypeError):
            card_1 = Card(1, 1)
        with self.assertRaises(TypeError):
            card_2 = Card('Diamond', 'Queen')

# checks values out of range
    def test_init_invalid_2(self):
        with self.assertRaises(ValueError):
            card_1 = Card('Diamond',0)
        with self.assertRaises(ValueError):
            card_2 = Card('Diamond',14)

# checks if suit is out of range
    def test_init_invalid_3(self):
        with self.assertRaises(ValueError):
            card_1 = Card('', 5)
        with self.assertRaises(ValueError):
            card_2 = Card('abc',5)

# checks if __gr__ is working right for value
    def test_gr_1(self):
        card_1 = Card('Club', 5)
        self.assertTrue(self.card > card_1)
        self.assertFalse(self.card < card_1)

# checks if __gr__ is working right for suit
    def test_gr_2(self):
        card_1 = Card('Diamond', 7)
        self.assertTrue(self.card > card_1)
        self.assertFalse(self.card < card_1)

#  checks if __eq__ is working right
    def test_eq_1(self):
        card_1 = Card('Club', 7)
        self.assertTrue(self.card == card_1)

# checks if __gr__ is working right for suit
    def test_eq_2(self):
        card_1 = Card('Diamond', 7)
        self.assertFalse(self.card == card_1)

# checks if __gr__ is working right for value
    def test_eq_3(self):
        card_1 = Card('Club', 8)
        self.assertFalse(self.card == card_1)







