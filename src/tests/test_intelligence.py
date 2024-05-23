import unittest
from src.intelligence import NPC

class TestNPC(unittest.TestCase):

    def setUp(self):
        self.npc = NPC("TestNPC", "medium")

    def test_initialization(self):
        self.assertEqual(self.npc.name, "TestNPC")
        self.assertEqual(self.npc.score, 0)
        self.assertEqual(self.npc.level, "medium")

    def test_change_level(self):
        new_level = "hard"
        self.npc.change_level(new_level)
        self.assertEqual(self.npc.level, new_level)

    def test_should_hold_easy(self):
        self.npc.change_level("easy")
        self.assertTrue(self.npc.should_hold(10))
        self.assertFalse(self.npc.should_hold(9))

    def test_should_hold_medium(self):
        self.assertTrue(self.npc.should_hold(20))
        self.assertFalse(self.npc.should_hold(19))

    def test_should_hold_hard(self):
        self.npc.change_level("hard")
        self.assertTrue(self.npc.should_hold(25))
        self.assertFalse(self.npc.should_hold(24))

if __name__ == '__main__':
    unittest.main()