import random

class Dice:
    """
    A class to represent a dice used in the dice game.

    Attributes:
        no_of_rolls (int): The number of times the dice has been rolled.
        turn_value (int): The accumulated value for the current turn.
    """
    def __init__(self):
        """
        Initializes the Dice with no rolls and zero turn value.
        """
        self.no_of_rolls = 0
        self.turn_value = 0

    def roll_dice(self):
        """
        Rolls the dice and updates the turn value.

        Returns:
            int: The result of the dice roll.
        """
        self.no_of_rolls += 1
        Value = random.randint(1, 6)
        self.turn_value += Value
        return Value
    
    def get_no_of_rolls(self):
        """
        Gets the number of rolls for the current turn.

        Returns:
            int: The number of rolls.
        """
        return self.no_of_rolls
    
    def get_turn_value(self):
        """
        Gets the turn value for the current turn.

        Returns:
            int: The turn value.
        """
        return self.turn_value