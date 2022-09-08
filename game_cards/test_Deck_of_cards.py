from unittest import TestCase
from unittest.mock import patch
from Deck_of_cards import DeckOfCards
from Card import Card


class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck_cards1 = DeckOfCards()
        self.card1 = Card("Diamond",1)

    """checks that there are 52 cards"""
    def test__init__valid_1(self):
        self.assertTrue(len(self.deck_cards1.list_cards) == 52)

    """checks that a card is in the stack"""
    def test__init__valid_2(self):
        self.assertIn(self.card1,self.deck_cards1.list_cards)

    """checks that the stack doesn't have an invalid number of cards """
    def test__init__invalid_1(self):
        self.assertFalse(len(self.deck_cards1.list_cards) == 51)

    """checks that the cards in the stack are in different places, because of the function cards_shuffle"""
    def test_cards_shuffle(self):
        deck_of_cards1 = DeckOfCards()
        deck_of_cards2 = DeckOfCards()
        deck_of_cards1.cards_shuffle()
        self.assertNotEqual(deck_of_cards2,deck_of_cards1)
        self.assertIn(self.card1,deck_of_cards1.list_cards)

    """a message will appear if there are no cards in the deck  """
    def test_deal_one_valid1(self):
        with self.assertRaises(ValueError):
            deck_cards = DeckOfCards()
            deck_cards.list_cards = []
            deck_cards.deal_one()

    """checks that the function deal_one removes a card from the stack. If the length of two lists is different 
    after deal_one worked, then a card was indeed removed"""
    def test_deal_one_invalid1(self):
        deck_of_card1 = DeckOfCards()
        deck_of_card2 = DeckOfCards()
        deck_of_card1.deal_one()
        self.assertNotEqual(len(deck_of_card1.list_cards),len(deck_of_card2.list_cards))













