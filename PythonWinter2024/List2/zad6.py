"""Napisz program, który pobiera od użytkownika dodatnią liczbę naturalną n i
tworzy listę o rozmiarze n × n. Program powinien wypełnić utworzoną listę tak,
aby a[i][j] = +, jeżeli liczby (i + 1) oraz (j + 1) są względnie pierwsze, tzn.
nie mają wspólnych dzielników poza 1. W pozostałych przypadkach a[i][j] = ..
Program powinien wypisać utworzoną listę na ekranie."""
import math


def coprime_matrix(n: int):
    # create matrix and fill: "+" if i+1, j+1 are coprime, "." if they're not
    mat = [["+" if (math.gcd(i + 1, j + 1) == 1) else "." for i in range(n)] for j in range(n)]

    # printing
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end=" ")
        print()


coprime_matrix(30)
