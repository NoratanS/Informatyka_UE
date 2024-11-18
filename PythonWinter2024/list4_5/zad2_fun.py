"""Zdefiniuj funkcję analiza(lst: list[int]) -> tuple[int, float, float] ,

która zwraca sumę, medianę oraz średnią elementów w liście lst . Wartości po-
winny być zwracane w postaci krotki (suma, mediana, średnia) .

Przykład użycia:
lst = [1, 3, 5, 7]
print(analiza(lst)) # Oczekiwany wynik: (16, 4.0, 4.0)"""
import statistics


def analyze_list_statistics(lst: list[int]) -> tuple[int, float, float]:
    return sum(lst), statistics.median(lst), float(statistics.mean(lst))


def analyze_list(lst: list[int]) -> tuple[int, float, float]:
    lst.sort()
    lst_len = len(lst)
    if lst_len % 2 == 0:
        median = (lst[lst_len // 2 - 1] + lst[lst_len // 2]) / 2
    else:
        median = lst[lst_len // 2]

    return sum(lst), median, sum(lst) / lst_len


lst = [1, 3, 5, 7]
print(analyze_list_statistics(lst))
print(analyze_list(lst))

