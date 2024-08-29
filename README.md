
# Tic-Tac-Toe Game in Python

This project implements a simple Tic-Tac-Toe game in Python using classes to manage the players, board, and game logic.

## How It Works

This game is played in the terminal, where two players take turns entering their moves. The game will update the board after each move and check for a win or tie condition.

### Player Class

```python
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
```

### Board Class

```python
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
```

### TicTacToe Class

```python
class TicTacToe:
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.win = False

    def check_win(self, marker):
        for i in range(3):
            if all(self.board.board[i][j] == marker for j in range(3)) or                all(self.board.board[j][i] == marker for j in range(3)):
                return True
        return all(self.board.board[i][i] == marker for i in range(3)) or                all(self.board.board[i][2-i] == marker for i in range(3))

    def play(self):
        self.board.show_board()
        while not self.win: 
            x, y = self.player1.move(self.board)
            self.board.update_board(x, y, self.player1.marker)
            self.board.show_board()
            self.win = self.check_win(self.player1.marker)
            if self.win: 
                print(f"{self.player1.name} wins!")
                break
            if self.board.is_full():
                print("It's a tie!")
                break
            x, y = self.player2.move(self.board)
            self.board.update_board(x, y, self.player2.marker)
            self.board.show_board()
            self.win = self.check_win(self.player2.marker)
            if self.win: 
                print(f"{self.player2.name} wins!")
        print("END")
```

### Running the Game

To start the game, we instantiate the players, the board, and the game, and then call the `play` method.

```python
player1 = Player("Anton", 'X')
player2 = Player("Anna", 'O')
board = Board()
game = TicTacToe(board, player1, player2)
game.play()
```

This setup allows two players to play Tic-Tac-Toe directly in the terminal. The game alternates turns between the players, updating the board after each move, and checking for a win or tie condition.

### Conclusion

Building a Tic-Tac-Toe game in Python using classes not only reinforces your understanding of object-oriented programming but also provides a fun project to enhance your problem-solving skills. By structuring your code with classes for the player, board, and game logic, you create a clean, modular, and maintainable codebase.

Whether you're a beginner or just brushing up on your skills, this project is a great exercise. Happy coding, and may the best player win!
