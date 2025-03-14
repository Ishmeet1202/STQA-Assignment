class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
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

    def reset_game(self):
        self.board = [" "] * 9
        self.current_player = "X"
        self.winner = None

    def make_move(self, position):
        index = position - 1

        if self.board[index] == " " and self.winner is None:
            self.board[index] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
                return f"Winner is {self.current_player}"
            elif " " not in self.board:
                self.winner = "Draw"
                return "Game Drawn!"
            else:
                if self.current_player == "X":
                    self.current_player = "O"
                else:
                    self.current_player = "X"
                return f"Next turn: {self.current_player}"
        else:
            return "Invalid Move!"

    def check_winner(self):
        return any(all(self.board[i] == self.current_player for i in case) for case in self.win_cases)