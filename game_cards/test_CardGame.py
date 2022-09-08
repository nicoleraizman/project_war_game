from unittest import TestCase
from CardGame import CardGame

from Deck_of_cards import DeckOfCards

class TestCardGame(TestCase):

    def setUp(self):
        self.game = CardGame('moshe', 'dani')

# checking if the init start all the functions
    def test_init_valid_1(self):
        game = CardGame('moshe','dani',26)
        self.assertEqual(game.name1, 'moshe')
        self.assertEqual(game.name2, 'dani')
        self.assertEqual(game.num_cards, 26)
        self.assertEqual(game.player1.name, 'moshe')
        self.assertEqual(game.player1.num_cards, 26)
        self.assertEqual(game.player2.name, 'dani')
        self.assertEqual(game.player2.num_cards, 26)
        self.assertEqual(len(game.player1.stack_cards), 26)
        self.assertEqual(len(game.player2.stack_cards), 26)

# checking if the build in of num_cards is 26
    def test_init_valid_2(self):
        self.assertEqual(self.game.num_cards, 26)

# checking if the is num_cards is out of range
    def test_init_valid_3(self):
        game_1 = CardGame('moshe', 'dani',9)
        game_2 = CardGame('moshe', 'dani',27)
        self.assertEqual(game_1.num_cards, 26)
        self.assertEqual(game_2.num_cards, 26)

# checks that the player can have any name
    def test_init_valid_4(self):
        game_1 = CardGame('1', '2', 26)
        self.assertEqual(game_1.name1, '1')
        self.assertEqual(game_1.name2, '2')

# checks tape of num_cards
    def test_init_invalid_1(self):
        with self.assertRaises(TypeError):
            game = CardGame('moshe', 'dani', '26')
# checks the stack_cards of players is not the same
    def test_new_game_1(self):
        self.assertNotEqual(self.game.player1.stack_cards, self.game.player2.stack_cards)

# checks the cards_shuffle work in new_game
    def test_new_game_2(self):
        dackcard = DeckOfCards()
        self.assertNotEqual(self.game.dack_of_card.list_cards, dackcard.list_cards)
# checks the new_game cant work out of init
    def test_new_game_invalid(self):
        with self.assertRaises(Exception):
            self.game.new_game()
# checks if ii is a tie
    def test_get_winner_1(self):
        self.assertEqual(self.game.get_winner(), None)

# checks if player 2 won
    def test_get_winner_2(self):
        self.game.player1.get_card()
        self.assertEqual(self.game.get_winner(), self.game.player2)

# checks if player 1 won
    def test_get_winner_3(self):
        self.game.player2.get_card()
        self.assertEqual(self.game.get_winner(), self.game.player1)



