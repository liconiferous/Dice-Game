import cmd
from game import Game
from highscore import HighScore
from player import Player
from intelligence import NPC

class GameCmd(cmd.Cmd):
    """
    Command-line interface for the dice game.
    """
    intro = "Welcome to the Dice Game! Type help or ? to list commands.\n"
    prompt = "(Game) "

    def __init__(self):
        """
        Initializes the command interface.
        """
        super().__init__()
        self.game = None
        self.highscores = HighScore()
        
    def do_start(self, arg):
        """
        Starts a new game with player names.
        Usage: start
        """
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
        """
        Plays a turn in the current game.
        Usage: play
        """
        if self.game:
            self.game.play_game()
        else:
            print("No game in progress. Use start to begin a new game.")

    def do_hold(self, arg):
        """
        Holds the current player's turn.
        Usage: hold
        """
        if self.game:
            self.game.hold()
            print(f"write 'play' for {self.game.current_player.name} to continue")
        else:
            print("No game in progress. Use start to begin a new game.")

    def do_reset(self, arg):
        """
        Resets the current game.
        Usage: reset
        """
        self.game.reset_game()
        print("Game has now been resetted, enter 'play' to start again")

    def do_cheat(self, arg):
        """
        Cheats by setting the current player's score.
        Usage: cheat [score]
        """
        if not arg:
            print("Missing argument - try 'cheat 100'")
            return

        score = int(arg)
        self.game.player1.score = score
        self.game.hold()

    def do_change_name(self, arg):
        """
        Changes the name of a player.
        Usage: change_name [old_name] [new_name]
        """
        if not arg:
            print("Missing argument - try 'change_name player1 player2'")
            return
        stuple = str.split(arg, " ")
        if self.game.player1.name == stuple[0]:
            self.game.player1.change_name(stuple[1])
        elif self.game.player2.name == stuple[0]:
            self.game.player2.change_name(stuple[1])
        else:
            print(f"No player by the name '{stuple[0]}' exist!")
            return
        print(f"player1 name: '{stuple[0]}' changed to: '{stuple[1]}'")

    def do_change_level(self, arg):
        """
        Changes the level of the NPC.
        Usage: change_level [easy/medium/hard]
        """
        if not arg:
            print("Missing argument - try 'change_level [easy/medium/hard]'")
            return
        if isinstance(self.game.player2, NPC):
            if arg == "easy" or arg == "medium" or arg == "hard":
                self.game.player2.change_level(arg)
            else:
                print(f"{arg} is not a valid level")
                return
            print(f"New level is: '{str(self.game.player2.get_level())}'")
        else:
            print("Player2 is not a NPC, level can not be changed")

    def do_highscores(self, arg):
        """
        Displays the high scores.
        Usage: highscores
        """
        self.highscores.display()

    def do_rules(self, arg):
        """
        Displays the rules of the dice game.
        Usage: rules
        """
        print("Pig is a simple dice game. Players take turns to roll a dice.")
        print("On each turn, a player rolls until they decide to hold or roll a 1.")
        print("If they roll a 1, they score nothing for that turn and it becomes the next player's turn.")
        print("If they hold, they add their turn total to their score.")
        print("First player to reach 100 points wins.")

    def do_help(self, arg):
        """
        Displays the help section with game commands.
        Usage: help
        """
        print('Help section - game commands')
        print('----------------------------')
        print('rules - shows the rules of the game')
        print('start - starts the game and let you register players')
        print('play - starts one turn of the game')
        print('hold - saves value to next player turn')
        print('reset - reset the game to start point')
        print('cheat - sets player score to entered value')
        print('change_name - let you change the name of a player')
        print('change_level - let you change the level of a NPC')
        print('highscores - shows the list of player highscore')
        print('quit - closes down the game')

    def do_quit(self, arg):
        """
        Quits the game.
        Usage: quit
        """
        print('Thank you for playing Pig!')
        return True