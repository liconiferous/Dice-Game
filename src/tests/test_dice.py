import unittest
from unittest.mock import patch
from src.dice import Dice

class TestDice(unittest.TestCase):

    def setUp(self):
        self.dice = Dice()

    def test_initialization(self):
        self.assertEqual(self.dice.no_of_rolls, 0)
        self.assertEqual(self.dice.turn_value, 0)

    @patch('random.randint', return_value=4)
    def test_roll_dice(self, mock_randint):
        result = self.dice.roll_dice()
        self.assertEqual(result, 4)
        self.assertEqual(self.dice.no_of_rolls, 1)
        self.assertEqual(self.dice.turn_value, 4)

    @patch('random.randint', side_effect=[3, 5, 2])
    def test_roll_dice_multiple_times(self, mock_randint):
        self.dice.roll_dice()
        self.dice.roll_dice()
        self.dice.roll_dice()
        self.assertEqual(self.dice.no_of_rolls, 3)
        self.assertEqual(self.dice.turn_value, 10)

    def test_get_no_of_rolls(self):
        self.assertEqual(self.dice.get_no_of_rolls(), 0)
        self.dice.roll_dice()
        self.assertEqual(self.dice.get_no_of_rolls(), 1)

    def test_get_turn_value(self):
        self.assertEqual(self.dice.get_turn_value(), 0)
        self.dice.roll_dice()
        self.assertTrue(self.dice.get_turn_value() > 0)

if __name__ == '__main__':
    unittest.main()
