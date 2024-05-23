from player import Player

class NPC(Player):
    """
    Represents a non-player character (NPC) in the dice game.

    Attributes:
        level (str): The difficulty level of the NPC.
    """
    def __init__(self, name, level='medium'):
        """
        Initializes a new NPC with the given name and difficulty level.

        Args:
            name (str): The name of the NPC.
            level (str): The difficulty level of the NPC ('easy', 'medium', 'hard').
        """
        super().__init__(name)
        self.level = level

    def should_hold(self, turn_total):
        """
        Determines whether the NPC should hold based on its difficulty level and the turn total.

        Args:
            turn_total (int): The total score for the current turn.

        Returns:
            bool: True if the NPC should hold, False otherwise.
        """
        if self.level == 'easy':
            return turn_total >= 10
        elif self.level == 'medium':
            return turn_total >= 20
        elif self.level == 'hard':
            return turn_total >= 25
        return False
    
    def change_level(self, level):
        """
        Changes the difficulty level of the NPC.

        Args:
            level (str): The new difficulty level for the NPC.
        """
        self.level = level

    def get_level(self):
        """
        Returns the difficulty level of the NPC.

        Returns:
            str: The difficulty level of the NPC.
        """
        return self.level