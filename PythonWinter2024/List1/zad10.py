"""Napisać program, który sprawdza, czy podana liczba całkowita n, n > 1, jest
liczbą pierwszą. Dodaj funkcjonalność wyświetlającą wszystkie liczby pierwsze w
zakresie od 1 do n"""
import math


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


def print_primes(n: int):  # TODO Eratosthenes
    for i in range(2, n + 1):
        if is_prime(i):
            print(i, end=' ')


print_primes(100)
