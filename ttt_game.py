class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    def move(self, board):
        while True:
            try:
                coord = input(f"{self.name}, enter coordinates (x y) in the range 1-3: ").split()
                if len(coord) != 2:
                    raise ValueError("Please enter two numbers separated by a space.")
                x, y = int(coord[0]) - 1, int(coord[1]) - 1
                if 0 <= x < 3 and 0 <= y < 3:
                    if board.is_empty(x, y):
                        return x, y
                    else:
                        print("That spot is already taken. Try again.")
                else:
                    print("Coordinates must be between 1 and 3. Try again.")
            except ValueError as e:
                print(f"Invalid input: {e}. Try again.")


class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def show_board(self):
        for i, row in enumerate(self.board):
            print(" | ".join(row))
            if i < 2:
                print("---------")

    def update_board(self, x, y, marker):
        if self.is_empty(x, y):
            self.board[x][y] = marker
            return True
        return False

    def is_empty(self, x, y):
        return self.board[x][y] == ' '

    def is_full(self):
        return all(cell != ' ' for row in self.board for cell in row)


class TicTacToe:
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.win = False

    def check_win(self, marker):
        for i in range(3):
            if all(self.board.board[i][j] == marker for j in range(3)) or \
               all(self.board.board[j][i] == marker for j in range(3)):
                return True
        return all(self.board.board[i][i] == marker for i in range(3)) or \
               all(self.board.board[i][2-i] == marker for i in range(3))

    def play(self):
        self.board.show_board()
        while not self.win: 
            x, y = self.player1.move(self.board)
            self.board.update_board(x, y, player1.marker)
            self.board.show_board()
            self.win = self.check_win(player1.marker)
            if self.win: 
                break
            x, y = self.player2.move(self.board)
            self.board.update_board(x, y, player2.marker)
            self.board.show_board()
            self.win = self.check_win(player2.marker)
        print("END")
        exit()


player1 = Player("anton", 'x')
player2 = Player("anna", 'o')
board = Board()
game = TicTacToe(board, player1, player2)
game.play()