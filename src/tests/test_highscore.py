import unittest
import os
import json
from src.highscore import HighScore
from src.player import Player

class TestHighScore(unittest.TestCase):

    def setUp(self):
        self.test_file_path = 'data/test_highscores.json'
        self.highscore = HighScore(self.test_file_path)
        self.player = Player("TestPlayer")
        self.game_winning_score = 100
        if not os.path.exists('data'):
            os.makedirs('data')

    def tearDown(self):
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_initialization(self):
        self.assertEqual(self.highscore.file_path, self.test_file_path)
        self.assertIsInstance(self.highscore.scores, dict)

    def test_load_scores_nonexistent_file(self):
        non_existent_path = 'data/non_existent.json'
        highscore = HighScore(non_existent_path)
        self.assertEqual(highscore.load_scores(), {})

    def test_save_scores(self):
        self.highscore.scores = {"TestPlayer": {"total_games": 1, "total_wins": 1, "highest_score": 100}}
        self.highscore.save_scores()
        with open(self.test_file_path, 'r') as f:
            data = json.load(f)
        self.assertEqual(data, self.highscore.scores)

    def test_update_new_player(self):
        self.player.score = 120
        self.highscore.update(self.player, self.game_winning_score)
        self.assertIn("TestPlayer", self.highscore.scores)
        self.assertEqual(self.highscore.scores["TestPlayer"]["total_games"], 1)
        self.assertEqual(self.highscore.scores["TestPlayer"]["total_wins"], 1)
        self.assertEqual(self.highscore.scores["TestPlayer"]["highest_score"], 120)

    def test_update_existing_player(self):
        self.player.score = 120
        self.highscore.update(self.player, self.game_winning_score)
        self.player.score = 90
        self.highscore.update(self.player, self.game_winning_score)
        self.assertEqual(self.highscore.scores["TestPlayer"]["total_games"], 2)
        self.assertEqual(self.highscore.scores["TestPlayer"]["total_wins"], 1)
        self.assertEqual(self.highscore.scores["TestPlayer"]["highest_score"], 120)

    def test_update_highest_score(self):
        self.player.score = 80
        self.highscore.update(self.player, self.game_winning_score)
        self.player.score = 150
        self.highscore.update(self.player, self.game_winning_score)
        self.assertEqual(self.highscore.scores["TestPlayer"]["highest_score"], 150)

    def test_display(self):
        self.player.score = 120
        self.highscore.update(self.player, self.game_winning_score)
        self.highscore.display()
        self.assertIn("TestPlayer", self.highscore.scores)
        self.assertEqual(self.highscore.scores["TestPlayer"]["highest_score"], 120)

if __name__ == '__main__':
    unittest.main()
