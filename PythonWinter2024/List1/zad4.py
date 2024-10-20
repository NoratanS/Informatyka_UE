"""Napisać program, który wczytuje od użytkownika liczbę całkowitą dodatnią n, a
następnie wyświetla na ekranie wszystkie potęgi liczby 2 nie większe, niż podana
liczba. Przykładowo, dla liczby 71 program powinien wyświetlić:
1
2
4
8
16
32
64
Dodaj możliwość wybrania dowolnej liczby bazowej, aby program wyświetlał jej
potęgi do określonej wartości."""


def powers():
    # Inputs
    n = int(input("Type a positive number (max): "))
    base = int(input("Type a positive number (base): "))

    # Check inputs
    if n < 0 or base < 0:
        print("Negative numbers are not allowed")
        powers()

    # initializing auxilary vars
    i = 0  # i stores the power index
    temp = base ** i  # Temp stores the power result

    # printing and calculating the next power until we reach max limit
    while temp <= n:
        print(temp)
        i += 1
        temp = base ** i


powers()
