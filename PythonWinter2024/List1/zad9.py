"""apisać program, dla podanej liczby całkowitej wyświetla jej dzielniki. Przykładowo, dla liczby 21 dzielniki to: 1, 3, 7, 21. Dodaj funkcję sprawdzającą, czy dana
liczba jest liczbą doskonałą (suma dzielników równa liczbie)."""


def print_factors(n: int):
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            print(i, end=", ")
    print(n)


def is_perfect(n: int) -> bool:
    f_sum = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            f_sum += i
    return f_sum == n


print_factors(21)

for i in range(1, 10000):
    if is_perfect(i):
        print(i)
