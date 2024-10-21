"""7. *Sito Eratostenesa

Napisz program, który implementuje algorytm Sita Eratostenesa w celu wyznacze-
nia liczb pierwszych z przedziału od 2 do n (gdzie n podaje użytkownik). Program

powinien wypisać wszystkie liczby pierwsze w tym przedziale.
https://pl.wikipedia.org/wiki/Sito_Eratostenesa"""

import math


def eratosthenes():
    n = int(input("Type a postive int: "))
    numbers = [True for i in range(n + 1)]
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if numbers[i]:
            for j in range(i * i, n + 1, i):
                numbers[j] = False

    for i in range(2, n + 1):
        if numbers[i]:
            print(i, end=' ')


eratosthenes()
