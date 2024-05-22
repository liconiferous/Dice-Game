import random

class Dice:
    def __init__(self):
        self.no_of_rolls = 0
        self.turn_value = 0

    def roll_dice(self):
        self.no_of_rolls += 1
        Value = random.randint(1, 6)
        self.turn_value += Value
        return Value
    
    def get_no_of_rolls(self):
        return self.no_of_rolls
    
    def get_turn_value(self):
        return self.turn_value