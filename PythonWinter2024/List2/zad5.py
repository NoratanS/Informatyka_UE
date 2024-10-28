"""Napisz program, w którym tworzona jest lista list (macierz) wypełniona losowymi
liczbami z zakresu [a, b], o wielkości n×n, gdzie wartości a, b oraz n są podawane
przez użytkownika.
Następnie program powinien wyznaczyć:
� sumę przekątnych (osobno dla każdej),
� sumę elementów leżących w listach o nieparzystych numerach indeksów i na
nieparzystych pozycjach (np. lista[1][1], lista[1][3], itd.),
� odwrócić wszystkie listy w macierzy (przykładowo, z [[1,2,3],[4,5,6],[7,8,9]]
na [[9,8,7],[6,5,4],[3,2,1]])."""
import random


def matrix_fun(a: int, b: int, n: int):
    # reversing the list and all the inner lists
    def reverse_list_rec(l: list):
        for i in range(len(l)):
            if isinstance(l[i], list):  # if list item is also a list we need to reverse it as well
                reverse_list_rec(l[i])
        l.reverse()  # reversing the list

    # create the matrix
    mat = [[random.randint(a, b) for _ in range(n)] for _ in range(n)]

    # calculate diagonal sums ()
    diag_sums = [0, 0]
    for i in range(n):
        for j in range(n):
            if i == j:  # first diagonal
                diag_sums[0] += mat[i][j]
            if i == n - j - 1:  # second diagonal
                diag_sums[1] += mat[i][j]

    # print
    for l in mat:
        print(l)
    print("Diagonal sums:")
    print(diag_sums)

    # reversing
    reverse_list_rec(mat)

    # printing reversed
    print("Reversed matrix:")
    for l in mat:
        print(l)
    return mat


matrix_fun(0, 9, 6)
