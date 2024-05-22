class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def reset_score(self):
        self.score = 0

    def update_stats(self, won=False):
        pass  # Implement as needed for additional player statistics

    def change_name(self, new_name):
        self.name = new_name