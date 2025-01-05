class TicTacToe:
    def __init__(self, size):
        self.__size = size
        self.__board = [[0 for _ in range(self.__size)] for _ in range(self.__size)]
        self.__players = {-1: "X",
                          0: "-",
                          1: "O"}

    def __print_board(self):
        for row in range(self.__size):
            for col in range(self.__size):
                print(self.__players[self.__board[row][col]], end=" ")
            print()

    def __move(self, player):
        def is_valid(row, col):
            available_numbers = [i for i in range(self.__size)]
            if row not in available_numbers or col not in available_numbers:
                return False

            if self.__board[row][col] != 0:
                return False
            return True

        def is_winning(row, col):
            to_win = self.__size

            # check row
            if abs(sum(self.__board[row])) == to_win:
                return True

            # check column
            col_sum = 0
            for i in range(to_win):
                col_sum += self.__board[i][col]
            if abs(col_sum) == to_win:
                return True

            # is on diagonal
            if row == col or row + col == to_win - 1:
                # if yes check diagonals
                diag1_sum = 0
                diag2_sum = 0
                for i in range(to_win):
                    diag1_sum += self.__board[i][i]
                    diag2_sum += self.__board[i][to_win - i - 1]
                if abs(diag1_sum) == to_win or abs(diag2_sum) == to_win:
                    return True

            return False

        player_move = input(
            "first number - row; second number - column; for example: 1 2 - first row and second column\n")
        row, col = int(player_move.split()[0]) - 1, int(player_move.split()[1]) - 1

        if is_valid(row, col):
            self.__board[row][col] += player
        else:
            print("Invalid move")
            self.__move(player)

        # is a winning move?
        if is_winning(row, col):
            return True
        else:
            return False

    def play(self):
        move_counter = 1
        winner = False
        player = -1

        while move_counter <= self.__size * self.__size:
            # move message
            print("Move " + str(move_counter))
            print(f"{self.__players[player]}'s turn")
            self.__print_board()
            # if it's a winning move the flag changes
            winner = self.__move(player)
            if winner:
                self.__print_board()
                print(f"Player {self.__players[player]} won!")
                break

            # if there's no winner move to next round
            move_counter += 1
            player *= -1

        if not winner:
            self.__print_board()
            print("It's a draw!")


game = TicTacToe(3)
game.play()
