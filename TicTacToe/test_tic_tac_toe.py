from game_logic import TicTacToe
import pytest

#Creating a Game Instance for Testing
@pytest.fixture
def game():
    return TicTacToe()

# Checks if the game starts with an empty board, "X" as the first player, and no winner.
def test_initial_state(game):
    assert game.board == [" "] * 9
    assert game.current_player == "X"
    assert game.winner is None

'''(i) Makes a valid move (position 1) 
    (ii) Ensures the board updates correctly
    (iii)Checks that the turn switches to "O" '''
def test_valid_move(game):
    result = game.make_move(1)
    assert game.board[0] == "X"
    assert result == "Next turn: O"
    assert game.current_player == "O"

'''(i)First move is valid (X plays at position 1).
   (ii) Second move tries to play at position 1 again (invalid).
   (iii) Checks that the board remains unchanged and turn remains O.'''
def test_invalid_move(game):
    game.make_move(1)
    result = game.make_move(1)
    assert result == "Invalid Move!"
    assert game.board[0] == "X"
    assert game.current_player == "O"

''' (i)Simulates a winning sequence for X (1,2,3 - top row).
    (ii)Ensures the game recognizes X as the winner.'''    
def test_winning_condition(game):
    game.make_move(1)  # X
    game.make_move(4)  # O
    game.make_move(2)  # X
    game.make_move(5)  # O
    result = game.make_move(3)  # X wins
    assert result == "Winner is X"
    assert game.winner == "X"

'''(i) Fills the board completely with no winner.
   (ii)Checks if the game correctly detects a draw.
   (iii)Ensures no more moves can be made after a draw.'''
def test_draw_condition(game):
    moves = [1, 2, 3, 5, 4, 6, 8, 7, 9]
    for move in moves:
        game.make_move(move)
    assert game.winner == "Draw"
    assert game.make_move(1) == "Invalid Move!"

# Makes some moves, then resets the game.(Checks if the game returns to its initial state.)
def test_reset_game(game):
    game.make_move(1)
    game.make_move(2)
    game.reset_game()
    assert game.board == [" "] * 9
    assert game.current_player == "X"
    assert game.winner is None

'''(i) Simulates a winning sequence for O (4,5,6 - middle row).
   (ii)Ensures the game recognizes O as the winner.'''
def test_winning_condition_O(game):
    game.make_move(1)  # X
    game.make_move(4)  # O
    game.make_move(2)  # X
    game.make_move(5)  # O
    game.make_move(9)  # X
    result = game.make_move(6)  # O wins
    assert result == "Winner is O"
    assert game.winner == "O"

#Preventing Additional Moves After Win (Ensures that after a win, no more moves can be made.)
def test_multiple_wins(game):
    game.make_move(1)  # X
    game.make_move(4)  # O
    game.make_move(2)  # X
    game.make_move(5)  # O
    game.make_move(3)  # X wins
    result = game.make_move(6)  # Game already won
    assert result == "Invalid Move!"
    assert game.winner == "X"

#Invalid Move After a Win (Ensures that if a player wins, any further moves are invalid.)
def test_invalid_move_after_win(game):
    game.make_move(1)  # X
    game.make_move(4)  # O
    game.make_move(2)  # X
    game.make_move(5)  # O
    game.make_move(3)  # X wins
    result = game.make_move(7)  # Invalid move after win
    assert result == "Invalid Move!"
    assert game.winner == "X"

# Testing Out-of-Bounds Move ( Checks if moves outside 1-9 are invalid.)
def test_invalid_move_out_of_bounds(game):
    result = game.make_move(10)  # Invalid move out of bounds
    assert result == "Invalid Move!"
    assert game.board == [" "] * 9
    assert game.current_player == "X"

#Testing Negative Move(Testing Negative Move)
def test_invalid_move_negative(game):
    result = game.make_move(-1)  # Invalid move negative
    assert result == "Invalid Move!"
    assert game.board == [" "] * 9
    assert game.current_player == "X"