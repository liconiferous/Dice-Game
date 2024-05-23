class Player:
    """
    Represents a player in the Pig dice game.

    Attributes:
        name (str): The name of the player.
        score (int): The player's current score.
    """
    def __init__(self, name):
        """
        Initializes a new player with the given name.

        Args:
            name (str): The name of the player.
        """
        self.name = name
        self.score = 0

    def reset_score(self):
        """
        Resets the player's score to zero.
        """
        self.score = 0

    def change_name(self, new_name):
        """
        Changes the player's name.

        Args:
            new_name (str): The new name for the player.
        """
        self.name = new_name