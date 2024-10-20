"""Napisać program, który pobiera od użytkownika liczbę całkowitą dodatnią, a na-
stępnie wyświetla na ekranie kolejno wszystkie liczby nieparzyste nie większe od

podanej liczby. Przykład, dla 15 program powinien wyświetlić 1, 3, 5, 7, 9, 11,
13, 15. Rozszerz zadanie, aby użytkownik podał dwie liczby, a program wyświetlił
wszystkie liczby nieparzyste w zakresie między tymi liczbami."""


def odds():
    # Inputs
    left = int(input("Left: "))
    right = int(input("Right: "))

    # Swap range ends if start is higher than the end
    if left > right:
        left, right = right, left

    # If we se start from an even number we have to increment it to make it odd
    # If the range end is odd we need to increment it so that the last number is included
    # If the range end is even its incrementation doesn't affect the result because of loop increment value (2)
    # for example if right = 16 the last number printed would be 15 because next number to check would be 17
    if left % 2 == 0:
        for i in range(left + 1, right + 1, 2):
            print(i, end=" ")
    else:
        for i in range(left, right + 1, 2):
            print(i, end=" ")


odds()
