import unittest
from src.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("TestPlayer")

    def test_initialization(self):
        self.assertEqual(self.player.name, "TestPlayer")
        self.assertEqual(self.player.score, 0)

    def test_reset_score(self):
        self.player.score = 50
        self.player.reset_score()
        self.assertEqual(self.player.score, 0)

    def test_change_name(self):
        new_name = "NewName"
        self.player.change_name(new_name)
        self.assertEqual(self.player.name, new_name)

    def test_update_stats(self):
        # Implement this test based on the implementation of update_stats
        pass

if __name__ == '__main__':
    unittest.main()