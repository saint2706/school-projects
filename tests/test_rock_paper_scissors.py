import pytest
from rock_paper_scissors import RockPaperScissorsGame

@pytest.fixture
def game():
    """Pytest fixture to create a RockPaperScissorsGame instance."""
    return RockPaperScissorsGame()

def test_determine_winner_tie(game):
    """Test the determine_winner method for a tie."""
    assert game.determine_winner("Rock", "Rock") == "Tie!"
    assert game.determine_winner("Paper", "Paper") == "Tie!"
    assert game.determine_winner("Scissors", "Scissors") == "Tie!"

def test_determine_winner_player_wins(game):
    """Test the determine_winner method for player wins."""
    assert "You win!" in game.determine_winner("Rock", "Scissors")
    assert "You win!" in game.determine_winner("Paper", "Rock")
    assert "You win!" in game.determine_winner("Scissors", "Paper")

def test_determine_winner_computer_wins(game):
    """Test the determine_winner method for computer wins."""
    assert "You lose!" in game.determine_winner("Rock", "Paper")
    assert "You lose!" in game.determine_winner("Paper", "Scissors")
    assert "You lose!" in game.determine_winner("Scissors", "Rock")

def test_get_computer_choice(game):
    """Test that the computer's choice is valid."""
    choice = game.get_computer_choice()
    assert choice in ["Rock", "Paper", "Scissors"]