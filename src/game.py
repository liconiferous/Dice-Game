from player import Player
from intelligence import NPC
from dice import Dice
from highscore import HighScore

class Game:
    WINNING_SCORE = 100

    def __init__(self, player1_name, player2_name=None, level='medium'):
        self.player1 = Player(player1_name)
        self.player2 = NPC(player2_name or "NPC", level=level) if not player2_name else Player(player2_name)
        self.current_player = self.player1
        self.dice = Dice()
        self.highscore = HighScore()

    def switch_player(self):
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2
        self.dice.turn_value = 0

    def play_turn(self):
        roll = self.dice.roll_dice()
        print(f"{self.current_player.name} rolled a {roll}")
        if roll == 1:
            print(f"{self.current_player.name} loses their turn!")
            self.switch_player()
            print(f"Press enter for {self.current_player.name} to continue")
        else:
            print(f"Turn total is now {self.dice.get_turn_value()}")
            if isinstance(self.current_player, NPC) and self.current_player.should_hold(self.dice.GetTotalValue()):
                self.hold()

    def hold(self):
        self.current_player.score += self.dice.get_turn_value()
        print(f"{self.current_player.name} holds. Total score is now {self.current_player.score}")
        if self.current_player.score >= self.WINNING_SCORE:
            print(f"{self.current_player.name} wins the game!")
            self.highscore.update(self.current_player, self.current_player.score)
            if not isinstance(self.current_player, NPC):
                self.highscore.update(self.current_player, self.current_player.score)
            else:
                self.highscore.update(self.current_player, self.current_player.score)
            self.reset_game()
        else:
            self.switch_player()

    def play_game(self):
            self.play_turn()
            if not isinstance(self.current_player, NPC) and self.dice.GetTotalValue() > 0:
                print('if you want to hold, write the command hold. Otherwise just hit enter to continue the turn')
