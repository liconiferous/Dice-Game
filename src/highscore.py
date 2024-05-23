import json
import os

class HighScore:
    """
    Manages the high scores for the dice game.

    Attributes:
        file_path (str): The path to the file where high scores are stored.
        scores (dict): The dictionary containing high scores data.
    """
    def __init__(self, file_path='src/data/highscores.json'):
        """
        Initializes the HighScore manager with a given file path.

        Args:
            file_path (str): The path to the high scores file.
        """
        self.file_path = file_path
        self.scores = self.load_scores()

    def load_scores(self):
        """
        Loads the high scores from the file.

        Returns:
            dict: The dictionary containing high scores data.
        """
        if not os.path.exists(self.file_path):
            print(f"Directory or file do not exist! {self.file_path}")
            return {}
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def save_scores(self):
        """
        Saves the current high scores to the file.
        """
        with open(self.file_path, 'w') as f:
            json.dump(self.scores, f, indent=4)

    def update(self, player, game_winning_score):
        """
        Updates the high scores with the latest game result.

        Args:
            player (Player): The player whose score needs to be updated.
            game_winning_score (int): The score required to win the game.
        """
        if player.name not in self.scores:
            self.scores[player.name] = {'total_games': 0, 'total_wins': 0, 'highest_score': 0}
        self.scores[player.name]['total_games'] += 1
        self.scores[player.name]['total_wins'] += 1 if player.score >= game_winning_score else 0
        self.scores[player.name]['highest_score'] = player.score if int(self.scores[player.name]['highest_score']) <= game_winning_score else int(self.scores[player.name]['highest_score'])
        self.save_scores()

    def display(self):
        """
        Displays the high scores.
        """
        self.scores = self.load_scores()
        print("High Scores:")
        for player, stats in self.scores.items():
            print(f"{player} - Games: {stats['total_games']}, Wins: {stats['total_wins']}, Highest: {stats['highest_score']}")