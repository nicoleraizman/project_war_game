from unittest import TestCase,mock
from unittest import TestCase
from Card import Card
from Player_ import Player
from Deck_of_cards import DeckOfCards

class TestPlayer(TestCase):
    def setUp(self):
        self.player1 = Player("Dani",11)
        self.player2 = Player("Dani")
        self.card1 = Card("Diamond", 2)

    """checks that the number of cards is not str"""
    def test__init__invalid_1(self):
        with self.assertRaises(TypeError):
            player2 = Player("Dani","abc")

    """checks that if you put cards more than 26, it will be 26 cards"""
    def test__init__valid1(self):
        p1 = Player("Dani",27)
        self.assertEqual(26,p1.num_cards)

    """checks that if you put cards lower than 10, it will be 26 cards"""
    def test__init__valid2(self):
        p2 = Player("Dani", 9)
        self.assertEqual(26, p2.num_cards)

    """checks that the default is 26 cards"""
    def test__init__valid_3(self):
        p3 = Player("Dani")
        self.assertEqual(26, p3.num_cards)

    """checks that the function set_hand gives cards to the player """
    @mock.patch('Deck_of_cards.DeckOfCards.deal_one',return_value=Card("Diamond",2))
    def test_set_hand(self,mock_deal_one):
        deck_cards1 = DeckOfCards()
        self.player1.set_hand(deck_cards1)
        self.assertIn(self.card1,self.player1.stack_cards)

    """checks that if a player has no cards, an error will be shown"""
    def test_get_card_invalid1(self):
        with self.assertRaises(ValueError):
            self.player1.stack_cards = []
            self.player1.get_card()

    """checks that a card was removed from a players stack"""
    def test_get_card_valid1(self):
        self.player1.stack_cards = [self.card1]
        self.player1.get_card()
        self.assertEqual([],self.player1.stack_cards)

    """checks that if get_card worked, and the card is still in the list, it is invalid"""
    def test_get_card_invalid2(self):
        self.player1.stack_cards = [self.card1]
        self.player1.get_card()
        self.assertNotEqual([self.card1],self.player1.stack_cards)

    """checks that a card was added to the players stack"""
    def test_add_card_valid1(self):
        self.player1.add_card(self.card1)
        self.assertEqual([self.card1],self.player1.stack_cards)

    """checks that if add_card worked, and a card was not added to the list, it is invalid"""
    def test_add_card_invalid1(self):
        self.player1.add_card(self.card1)
        self.assertNotEqual([], self.player1.stack_cards)
