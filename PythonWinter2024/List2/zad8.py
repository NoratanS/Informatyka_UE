"""Napisz program, który rozwiązuje problem ośmiu hetmanów, polegający na umiesz-
czeniu ośmiu hetmanów na szachownicy 8x8 w taki sposób, aby żaden hetman nie

atakował innego. Program powinien znaleźć i wypisać wszystkie możliwe rozwią-
zania.

https://pl.wikipedia.org/wiki/Problem_o%C5%9Bmiu_hetman%C3%B3w"""


def solveNQueens(n):
    def could_place(row, col):
        for i in range(row):
            if board[i] == col or \
                    board[i] - i == col - row or \
                    board[i] + i == col + row:
                return False
        return True

    def place_queens(n, row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if could_place(row, col):
                board[row] = col
                place_queens(n, row + 1)
                board[row] = 0

    result = []
    board = [0] * n
    place_queens(n, 0)
    return [[i for i in sol] for sol in result]


print(solveNQueens(4))
