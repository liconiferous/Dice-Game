from player import Player

class NPC(Player):
    def __init__(self, name, level='medium'):
        super().__init__(name)
        self.level = level

    def should_hold(self, turn_total):
        if self.level == 'easy':
            return turn_total >= 10
        elif self.level == 'medium':
            return turn_total >= 20
        elif self.level == 'hard':
            return turn_total >= 25
        return False
    
    def change_level(self, level):
        self.level = level

    def get_level(self):
        return self.level