"""Napisz program, który utworzy listę 20 liczb całkowitych z przedziału 1 . . . 10, a
następnie wypisze, ile razy każda z liczb z tego przedziału powtarza się w liście.
Przykładowy wynik:
Wylosowane liczby: 6 5 4 5 10 5 8 3 10 6 6 6 4 3 2 8 1 3 4 7
Wystąpienia:
1 - 1
2 - 1
3 - 3
4 - 3
5 - 3

4

6 - 4
7 - 1
8 - 2
9 - 0
10 - 2"""
import random


def list_count_digits(l: list, start: int, end: int) -> list:
    # counting
    counts = [0 for i in range(start, end+1)]
    for i in l:
        counts[i - start] += 1

    # printing
    for i in range(start, end+1):
        print(f"{i} - {counts[i - start]}")

    return counts


l = [random.randint(1, 10) for i in range(20)]
print(l)
list_count_digits(l, 1, 10)


