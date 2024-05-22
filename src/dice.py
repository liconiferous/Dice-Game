import random

class Dice:
    def __init__(self):
        self.NoofRolls = 0
        self.TotalValue = 0

    def RollDice(self):
        self.NoofRolls += 1
        Value = random.randint(1, 6)
        self.TotalValue += Value
        return Value
    
    def GetNoofRolls(self):
        return self.NoofRolls
    
    def GetTotalValue(self):
        return self.TotalValue


