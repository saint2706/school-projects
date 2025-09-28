import pytest
from unittest.mock import patch
from blackjack24 import BlackjackGame

@pytest.fixture
def game():
    """Pytest fixture to create a BlackjackGame instance."""
    return BlackjackGame()

def test_calculate_score_blackjack(game):
    """Test score calculation for a blackjack hand."""
    assert game._calculate_score([11, 10]) == 0

def test_calculate_score_regular(game):
    """Test score calculation for a regular hand."""
    assert game._calculate_score([10, 5]) == 15

def test_calculate_score_with_ace(game):
    """Test score calculation with an ace as 11."""
    assert game._calculate_score([11, 5]) == 16

def test_calculate_score_with_ace_as_one(game):
    """Test score calculation with an ace as 1."""
    assert game._calculate_score([11, 10, 5]) == 16

def test_calculate_score_multiple_aces(game):
    """Test score calculation with multiple aces."""
    assert game._calculate_score([11, 11, 5]) == 17

def test_compare_scores_draw(game):
    """Test score comparison for a draw."""
    assert game._compare_scores(20, 20) == "It's a draw."

def test_compare_scores_computer_blackjack(game):
    """Test score comparison when the computer has blackjack."""
    assert game._compare_scores(20, 0) == "You lose, opponent has Blackjack."

def test_compare_scores_user_blackjack(game):
    """Test score comparison when the user has blackjack."""
    assert game._compare_scores(0, 20) == "You win with a Blackjack!"

def test_compare_scores_user_bust(game):
    """Test score comparison when the user busts."""
    assert game._compare_scores(22, 20) == "You went over. You lose."

def test_compare_scores_computer_bust(game):
    """Test score comparison when the computer busts."""
    assert game._compare_scores(20, 22) == "Opponent went over. You win."

def test_compare_scores_user_wins(game):
    """Test score comparison when the user has a higher score."""
    assert game._compare_scores(20, 18) == "You win."

def test_compare_scores_user_loses(game):
    """Test score comparison when the user has a lower score."""
    assert game._compare_scores(18, 20) == "You lose."

@patch('builtins.input', side_effect=['n'])
@patch('blackjack24.random.choice', side_effect=[10, 8, 5, 10])
def test_play_game_stand(mock_random_choice, mock_input, game, capsys):
    """Test a full game flow where the user stands."""
    game.play()
    captured = capsys.readouterr()
    assert "Your final hand: [10, 5], final score: 15" in captured.out
    assert "Computer's final hand: [8, 10], final score: 18" in captured.out
    assert "You lose." in captured.out