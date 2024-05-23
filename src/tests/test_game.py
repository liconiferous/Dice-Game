import unittest
from unittest.mock import patch
from src.game import Game
from src.player import Player
from src.intelligence import NPC

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game("Player1", "Player2")
        self.npc_game = Game("Player1")

    def test_initialization(self):
        self.assertEqual(self.game.player1.name, "Player1")
        self.assertEqual(self.game.player2.name, "Player2")
        self.assertIsInstance(self.npc_game.player2, NPC)
        self.assertEqual(self.npc_game.player2.name, "NPC")

    @patch('src.dice.Dice.roll_dice', return_value=5)
    def test_play_turn(self, mock_roll):
        self.game.play_turn()
        self.assertEqual(self.game.dice.get_turn_value(), 5)
        self.assertEqual(self.game.current_player, self.game.player1)

    @patch('src.dice.Dice.roll_dice', return_value=1)
    def test_play_turn_roll_one(self, mock_roll):
        with patch('builtins.print'):
            self.game.play_turn()
        self.assertEqual(self.game.dice.get_turn_value(), 0)
        self.assertEqual(self.game.current_player, self.game.player2)

    def test_switch_player(self):
        self.game.switch_player()
        self.assertEqual(self.game.current_player, self.game.player2)
        self.game.switch_player()
        self.assertEqual(self.game.current_player, self.game.player1)

    @patch('src.dice.Dice.get_turn_value', return_value=50)
    def test_hold(self, mock_turn_value):
        self.game.hold()
        self.assertEqual(self.game.player1.score, 50)
        self.assertEqual(self.game.current_player, self.game.player2)

    @patch('src.dice.Dice.get_turn_value', return_value=100)
    def test_hold_and_win(self, mock_turn_value):
        with patch('builtins.print'):
            self.game.hold()
        self.assertEqual(self.game.player1.score, 100)
        self.assertEqual(self.game.player2.score, 0)
        self.assertEqual(self.game.current_player, self.game.player1)

    def test_reset_game(self):
        self.game.player1.score = 50
        self.game.player2.score = 60
        self.game.reset_game()
        self.assertEqual(self.game.player1.score, 0)
        self.assertEqual(self.game.player2.score, 0)
        self.assertEqual(self.game.dice.turn_value, 0)
        self.assertEqual(self.game.current_player, self.game.player1)

if __name__ == '__main__':
    unittest.main()
