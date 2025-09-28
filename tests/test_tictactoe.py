import pytest
from tictactoe import TicTacToe

@pytest.fixture
def game():
    """Pytest fixture to create a TicTacToe instance."""
    return TicTacToe()

def test_initial_state(game):
    """Test the initial state of the game."""
    assert all(cell is None for cell in game.board)
    assert game.current_player == "X"
    assert game.game_state == "RUNNING"

def test_make_valid_move(game):
    """Test making a valid move."""
    assert game.make_move(0)
    assert game.board[0] == "X"
    assert game.current_player == "O"
    assert game.game_state == "RUNNING"

def test_make_invalid_move_out_of_bounds(game):
    """Test making a move that is out of bounds."""
    assert not game.make_move(9)
    assert game.current_player == "X"

def test_make_invalid_move_occupied(game):
    """Test making a move on an occupied cell."""
    game.make_move(0)
    assert not game.make_move(0)
    assert game.current_player == "O"

def test_switch_player(game):
    """Test switching the player."""
    game.switch_player()
    assert game.current_player == "O"
    game.switch_player()
    assert game.current_player == "X"

def test_win_horizontal(game):
    """Test a horizontal win."""
    game.board = ["X", "X", "X", None, None, None, None, None, None]
    game.update_game_state()
    assert game.game_state == "WIN"

def test_win_vertical(game):
    """Test a vertical win."""
    game.board = ["X", None, None, "X", None, None, "X", None, None]
    game.update_game_state()
    assert game.game_state == "WIN"

def test_win_diagonal(game):
    """Test a diagonal win."""
    game.board = ["X", None, None, None, "X", None, None, None, "X"]
    game.update_game_state()
    assert game.game_state == "WIN"

def test_draw(game):
    """Test a draw condition."""
    game.board = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
    game.update_game_state()
    assert game.game_state == "DRAW"

def test_get_valid_moves(game):
    """Test getting a list of valid moves."""
    game.board = ["X", "O", "X", None, "O", None, None, "X", None]
    assert game.get_valid_moves() == [3, 5, 6, 8]