import cmd
from game import Game
from highscore import HighScore
from player import Player
from intelligence import NPC

class GameCmd(cmd.Cmd):
    intro = "Welcome to the Pig Game! Type help or ? to list commands.\n"
    prompt = "(Game) "

    def __init__(self):
        super().__init__()
        self.game = None
        self.highscores = HighScore()
        
    def do_start(self, arg):
        player1 = str(input("enter player1 name: "))
        player2 = str(input("enter player2 name (just leave blank for playing against computer): "))
        self.player1 = Player(player1)
        self.player2 = NPC(player2 or "NPC", level="medium") if not player2 else Player(player2)
        
        if player2 == "" and player1 == "":
            print("Thank you for playing Pig!")
            return True
        elif player2 == "":
            self.game = Game(player1, None, level="medium")
            print(f"Current player is '{player1}'")
        else:
            self.game = Game(player1, player2)
            print(f"Current player is '{player1}' and '{player2}'")

    def do_play(self, arg):
        if self.game:
            self.game.play_game()
        else:
            print("No game in progress. Use start to begin a new game.")

    def do_hold(self, arg):
        if self.game:
            self.game.hold()
            print(f"write 'play' for {self.game.current_player.name} to continue")
        else:
            print("No game in progress. Use start to begin a new game.")

    def do_reset(self, arg):
        self.game.reset_game()
        print("Game has now been resetted, enter 'play' to start again")

    def do_cheat(self, arg):
        if not arg:
            print("Missing argument - try 'cheat 100'")
            return

        score = int(arg)
        self.game.player1.score = score
        self.game.hold()

    def do_highscores(self, arg):
        self.highscores.display()

    def do_rules(self, arg):
        print("Pig is a simple dice game. Players take turns to roll a dice.")
        print("On each turn, a player rolls until they decide to hold or roll a 1.")
        print("If they roll a 1, they score nothing for that turn and it becomes the next player's turn.")
        print("If they hold, they add their turn total to their score.")
        print("First player to reach 100 points wins.")

    def do_quit(self, arg):
        print('Thank you for playing Pig!')
        return True