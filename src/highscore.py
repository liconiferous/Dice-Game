import json
import os

class HighScore:
    def __init__(self, file_path='data/highscores.json'):
        self.file_path = file_path
        self.scores = self.load_scores()

    def load_scores(self):
        if not os.path.exists(self.file_path):
            return {}
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def save_scores(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.scores, f, indent=4)

    def update(self, player, game_winning_score):
        if player.name not in self.scores:
            self.scores[player.name] = {'total_games': 0, 'total_wins': 0, 'highest_score': 0}
        self.scores[player.name]['total_games'] += 1
        self.scores[player.name]['total_wins'] += 1 if player.score >= game_winning_score else 0
        self.scores[player.name]['highest_score'] = player.score if int(self.scores[player.name]['highest_score']) >= game_winning_score else 0
        self.save_scores()

    def display(self):
        self.scores = self.load_scores()
        print("High Scores:")
        for player, stats in self.scores.items():
            print(f"{player} - Games: {stats['total_games']}, Wins: {stats['total_wins']}, Highest: {stats['highest_score']}")