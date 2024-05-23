import unittest
from unittest.mock import patch, MagicMock
from src.cmd_interface import GameCmd

class TestGameCmd(unittest.TestCase):

    def setUp(self):
        self.cmd = GameCmd()

    @patch('builtins.input', side_effect=['player1', ''])
    @patch('game.Game')
    def test_start_game_single_player(self, mock_game, mock_input):
        self.cmd.do_start('')
        self.assertIsNotNone(self.cmd.game)
        self.assertEqual(mock_game.call_count, 1)

    @patch('builtins.input', side_effect=['player1', 'player2'])
    @patch('game.Game')
    def test_start_game_two_players(self, mock_game, mock_input):
        self.cmd.do_start('')
        self.assertIsNotNone(self.cmd.game)
        self.assertEqual(mock_game.call_count, 1)

    def test_play_no_game(self):
        with patch('sys.stdout', new_callable=unittest.mock.MagicMock()) as mock_stdout:
            self.cmd.do_play('')
            mock_stdout.write.assert_called_with("No game in progress. Use start to begin a new game.\n")

    @patch('game.Game.play_game')
    def test_play_game(self, mock_play_game):
        self.cmd.game = MagicMock()
        self.cmd.do_play('')
        mock_play_game.assert_called_once()

    def test_hold_no_game(self):
        with patch('sys.stdout', new_callable=unittest.mock.MagicMock()) as mock_stdout:
            self.cmd.do_hold('')
            mock_stdout.write.assert_called_with("No game in progress. Use start to begin a new game.\n")

    @patch('game.Game.hold')
    def test_hold_game(self, mock_hold):
        self.cmd.game = MagicMock()
        self.cmd.do_hold('')
        mock_hold.assert_called_once()

    @patch('game.Game.reset_game')
    def test_reset_game(self, mock_reset_game):
        self.cmd.game = MagicMock()
        with patch('sys.stdout', new_callable=unittest.mock.MagicMock()) as mock_stdout:
            self.cmd.do_reset('')
            mock_reset_game.assert_called_once()
            mock_stdout.write.assert_called_with("Game has now been reset, enter 'play' to start again\n")

    def test_cheat_no_arg(self):
        with patch('sys.stdout', new_callable=unittest.mock.MagicMock()) as mock_stdout:
            self.cmd.do_cheat('')
            mock_stdout.write.assert_called_with("Missing argument - try 'cheat 100'\n")

    def test_cheat_with_arg(self):
        self.cmd.game = MagicMock()
        with patch('game.Game.hold') as mock_hold:
            self.cmd.do_cheat('100')
            self.assertEqual(self.cmd.game.current_player.score, 100)
            mock_hold.assert_called_once()

    def test_quit(self):
        with patch('sys.stdout', new_callable=unittest.mock.MagicMock()) as mock_stdout:
            result = self.cmd.do_quit('')
            mock_stdout.write.assert_called_with("Thank you for playing Pig!\n")
            self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
