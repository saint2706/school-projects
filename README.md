# School Computer Science Projects

This repository is a collection of computer science projects created by students. The projects have been refactored and modernized to follow best practices.

## Getting Started

To run these projects, you will need to have Python installed on your system. You will also need to install the required libraries.

### Prerequisites

*   Python 3.x
*   pip

### Installation

1.  Clone the repository to your local machine:
    ```bash
    git clone <repository-url>
    ```
2.  Navigate to the project directory:
    ```bash
    cd <repository-name>
    ```
3.  Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Projects

To run a project, simply execute the corresponding Python script from your terminal:

```bash
python <filename.py>
```

For example, to run the Blackjack game:
```bash
python blackjack24.py
```

## Testing

This project uses `pytest` for testing. To run the tests, first install the development dependencies:

```bash
pip install pytest
```

Then, run the test suite from the root of the repository:

```bash
PYTHONPATH=. pytest
```

## Continuous Integration

This repository uses GitHub Actions to automatically run tests on every push and pull request. This ensures that all changes are validated and that the codebase remains stable.

## Projects

| Project Name                      | Original Author(s) | New Filename                            | Description                                                               |
| --------------------------------- | ------------------ | --------------------------------------- | ------------------------------------------------------------------------- |
| Blackjack                         | Somesh Jadhwani    | `blackjack24.py`                        | A command-line based Blackjack game.                                      |
| Minesweeper                       | Rishabh            | `minesweeper_tkinter.py`                | A GUI-based Minesweeper game with a modern "Material You" look and feel.  |
| Encrypt/Decrypt                   | Aryav Shrivastava  | `encrypt_decrypt.py`                    | A tool to encrypt and decrypt text using a simple substitution cipher.    |
| Guess the Room                    | Aryav Shrivastava  | `guess_the_room.py`                     | A command-line based guessing game with an ASCII art map.                 |
| Personal Assistant                | Aaryan H           | `personal_assistant.py`                 | A simple personal assistant that can tell jokes, act as a magic 8-ball, and spin a wheel. |
| Rock, Paper, Scissors, Lizard, Spock | Aaryan H        | `rock_paper_scissors_lizard_spock.py`   | A command-line based Rock, Paper, Scissors, Lizard, Spock game.           |
| Secret Santa                      | Aaryan H           | `secret_santa.py`                       | A Secret Santa organizer.                                                 |
| Poker                             | Rohan S            | `poker/`                                | A refactored, modular poker game.                                         |
| Battleship                        | Aniruddh Dewri     | `battleship.py`                         | A single-player Battleship game.                                          |
| Board Game                        | Ankitha            | `board_game.py`                         | A simple board game.                                                      |
| FIFA 2019                         | Hänan Basheer      | `fifa/`                                 | A refactored, modular soccer simulation game.                             |
| Hangman                           | Multiple Authors   | `hangman.py`                            | A feature-rich hangman game with multiple modes.                          |
| Mad Libs                          | Rishabh            | `mad_libs.py`                           | A Mad Libs game with multiple stories.                                    |
| Mastermind                        | Aayush Rajesh      | `mastermind.py`                         | A Mastermind game where the player has to guess a 6-color code.           |
| Meal Planner                      | Akshat Singh       | `meal_planner.py`                       | A simple meal planner based on user preferences.                          |
| Morse Code Converter              | Multiple Authors   | `morse_converter.py`                    | A tool to convert text to and from Morse code, with multiple ciphers.     |
| Rock, Paper, Scissors             | Utsav Doshi        | `rock_paper_scissors.py`                | A command-line based Rock, Paper, Scissors game.                          |
| Password Generator                | Utsav Doshi        | `password_generator.py`                 | A tool to generate random passwords.                                      |
| Snakes and Ladders                | Avi and Rishabh    | `snakes_and_ladders.py`                 | A Snakes and Ladders game with a graphical board.                         |
| Tic-Tac-Toe                       | Rishabh            | `tictactoe.py`                          | A Tic-Tac-Toe game with player-vs-player and player-vs-computer modes.    |
| UNO                               | Rishabh, Swathi    | `uno.py`                                | A feature-rich UNO game with a text-based GUI.                            |
| Cricket                           | Kingshuk           | `cricket.py`                            | A simple cricket game.                                                    |
| Encryptor                         | Somesh Jadhwani    | `encryptor24.py`                        | A simple substitution cipher.                                             |
| Word Guessing Game                | Sushree            | `word_guessing_game.py`                 | A word guessing game with hints.                                          |
| Word Jumble                       | Sushree            | `word_jumble.py`                        | A word jumble game with hints.                                            |
| Magic 8-Ball                      | Kingshuk, Rishabh  | `magic_8_ball.py`                       | A Magic 8-Ball game with a "roast me" feature.                            |
| Password Manager                  | Anisha Katiyar     | `password_manager.py`                   | A simple password manager.                                                |
| Lunar Survival                    | Anisha Katiyar     | `lunar_survival.py`                     | A text-based lunar survival game.                                         |
| Simple Encrypt                    | Siddhant Saxena    | `simple_encrypt.py`                     | A simple encryption/decryption script.                                    |
| Number Guesser                    | Siddhant Saxena    | `number_guesser.py`                     | A number guessing game.                                                   |
| Riddle Game                       | Siddhant Saxena    | `riddle_game.py`                        | A riddle game.                                                            |
| Snake Ludo                        |                    | `snake_ludo.py`                         | A simple Snakes and Ladders game.                                         |
