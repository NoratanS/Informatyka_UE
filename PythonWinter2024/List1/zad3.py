"""Napisać program, który pobiera od użytkownika liczbę całkowitą dodatnią, a na-
stępnie wyświetla na ekranie kolejno wszystkie liczby nieparzyste nie większe od

podanej liczby. Przykład, dla 15 program powinien wyświetlić 1, 3, 5, 7, 9, 11,
13, 15. Rozszerz zadanie, aby użytkownik podał dwie liczby, a program wyświetlił
wszystkie liczby nieparzyste w zakresie między tymi liczbami."""


def odds():
    left = int(input("Left: "))
    right = int(input("Right: "))

    if left > right:
        left, right = right, left

    if left % 2 == 1:
        for i in range(left, right + 1, 2):
            print(i, end=" ")
    else:
        for i in range(left + 1, right + 1, 2):
            print(i, end=" ")


odds()
