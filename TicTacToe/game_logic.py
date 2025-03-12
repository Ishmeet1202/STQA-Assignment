class TicTacToe:
    # Class Initialization (__init__ method)
    def __init__(self):
        self.board = [" "] * 9  # Creates a list of 9 empty spaces to represent a 3x3 Tic-Tac-Toe board.
        self.current_player = "X"
        self.winner = None
        self.win_cases = [
            [0, 1, 2],  # Rows
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],  # Columns
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],  # Diagonals
            [2, 4, 6]
        ]

    # Resetting the Game 
    def reset_game(self):
        self.board = [" "] * 9
        self.current_player = "X"
        self.winner = None

    # Checking If a Move Is Valid (is_valid_move method)
    def is_valid_move(self, position):
        """Helper function to check if a move is valid"""
        return 1 <= position <= 9 and self.board[position - 1] == " "

    def make_move(self, position):
        """Handles player moves"""
        if self.winner:  # Prevent moves after game is won
            return "Invalid Move!"  # Change from "Game already won!" to "Invalid Move!"

        if not self.is_valid_move(position):
            return "Invalid Move!"

        index = position - 1
        self.board[index] = self.current_player

        if self.check_winner():
            self.winner = self.current_player
            return f"Winner is {self.current_player}"

        if " " not in self.board:
            self.winner = "Draw"
            return "Game Drawn!"

        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"
        return f"Next turn: {self.current_player}"


    def check_winner(self):
        """Checks if the current player has won."""
        return any(all(self.board[i] == self.current_player for i in case) for case in self.win_cases)
