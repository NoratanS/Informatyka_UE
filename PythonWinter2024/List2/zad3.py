"""Napisz program, który:
� stworzy listę list (macierz) 5 x 5 liczb całkowitych wylosowanych z zakresu
{−5, −4, . . . , 5},
� dla każdej kolumny wyznaczy minimum,
� dla każdej kolumny wyznaczy maksimum.

Program powinien wyświetlić macierz wypełnioną liczbami oraz tablice z mini-
mami i maksymami."""

#TODO: try without transpozing
import random


def random_matrix(n: int, start: int, end: int):
    # initialize matrix (n x n) with random numbers (start, end)
    matrix = [[random.randint(start, end) for _ in range(n)] for _ in range(n)]
    matrix_transpozed = [[matrix[j][i] for j in range(n)] for i in range(n)]
    min_col = [min(l) for l in matrix_transpozed]
    max_col = [max(l) for l in matrix_transpozed]

    print("Matrix:")
    for l in matrix:
        print(l)
    print("Matrix_t:")
    for l in matrix_transpozed:
        print(l)
    print(f"\nMinimums in each column: {min_col}")
    print(f"\nMaximums in each column: {max_col}")


random_matrix(5, -5, 5)
