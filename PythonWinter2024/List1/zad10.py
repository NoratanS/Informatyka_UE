"""Napisać program, który sprawdza, czy podana liczba całkowita n, n > 1, jest
liczbą pierwszą. Dodaj funkcjonalność wyświetlającą wszystkie liczby pierwsze w
zakresie od 1 do n"""
import math
import numbers


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


def print_primes(n: int):
    for i in range(2, n + 1):
        if is_prime(i):
            print(i, end=' ')


def eratosthenes(n: int):
    numbers = [True for i in range(n + 1)]
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if numbers[i]:
            for j in range(i * i, n + 1, i):
                numbers[j] = False

    for i in range(2, n + 1):
        if numbers[i]:
            print(i, end=' ')


def primes_oneline(n: int) -> list:
    return [i for i in range(2, n + 1) if not any(i % j == 0 for j in range(2, math.floor(math.sqrt(i)) + 1))]


print(f"2137: {is_prime(2137)}")
print_primes(101)
print()
eratosthenes(101)
print()
print(primes_oneline(101))
