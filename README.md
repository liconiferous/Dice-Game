# Dice-Game

Welcome to the Dice Game! This project implements the classic dice game "Pig" with a command-line interface. You can play against another player or against the computer.

## Table of Contents
- [Game Rules](#game-rules)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Intelligence Implementation](#intelligence-implementation)
- [Unit Testing](#unit-testing)
- [Code Style and Linting](#code-style-and-linting)

## Game Rules

Pig is a simple dice game where players take turns to roll a single dice. The goal is to be the first to reach 100 points. 
On each turn, a player can roll the dice as many times as they wish, adding the result to their turn total. 
However, if they roll a 1, they lose all points accumulated in that turn and it becomes the next player's turn. 
Players can choose to "hold" their current turn total, adding it to their overall score, and pass the die to the next player.
The first player to reach 100 points wins.

## Installation

To run the Pig Dice Game on your local machine, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/liconiferous/Dice-Game.git
    cd dice-game
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the game, run:
```bash
python src/main.py
```
You will be prompted to enter player names. You can leave the second player name blank to play against the computer.

Game Commands
start: Starts a new game and registers players.
play: Starts one turn of the game.
hold: Ends the current player's turn and adds their turn total to their overall score.
reset: Resets the game to the starting point.
cheat [score]: Sets the current player's score to the specified value.
change_name [old_name] [new_name]: Changes the name of a player.
change_level [easy/medium/hard]: Changes the difficulty level of the NPC.
highscores: Displays the list of player high scores.
rules: Displays the rules of the game.
help: Lists all available commands.
quit: Closes down the game.

## Project structure

├── src
│	├──	data
│   │	└── highscores.json
│   ├── cmd_interface.py
│   ├── dice.py
│   ├── game.py
│   ├── highscore.py
│   ├── intelligence.py
│   ├── player.py
│   ├── main.py
│	└── tests
│   	├── test_cmd_interface.py
│   	├── test_dice.py
│   	├── test_game.py
│   	├── test_highscore.py
│   	├── test_intelligence.py
│   	└── test_player.py
├── .flake8
├── .pylintrc
├── Makefile
├── README.md
└── requirements.txt

## Intelligence implemention

The intelligence part of the game is implemented in the NPC class within intelligence.py. 
The NPC class simulates a computer player with three levels of difficulty: easy, medium, and hard. 
The decision-making process for the NPC involves evaluating the current turn total and the risk of rolling a 1. 
The NPC will decide whether to roll again or hold based on the difficulty level and the current game state.

## Unit testing

Unit tests are provided to ensure the functionality of each component of the game. The tests are located in the tests directory and cover all main classes and modules.

To run the unit tests, execute:
```bash
make test
```

To generate a test coverage report, execute:
```bash
make coverage
```

## Code Style and Linting

This project uses pylint and flake8 with flake8-docstrings and flake8-polyfill to enforce code style and avoid bad coding practices.

To run the linters, execute:
```bash
make lint
```