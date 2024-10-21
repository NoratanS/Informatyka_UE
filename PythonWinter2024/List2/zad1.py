"""1. Napisz program, który:

� utworzy listę 10 liczb całkowitych i wypełni ją wartościami losowymi z prze-
działu [−10, . . . , 10],

� wypisze na ekranie zawartość listy,

� wyznaczy najmniejszy oraz największy element w liście (za pomocą wbudo-
wanych funkcji oraz własnej implementacji),

� wyznaczy średnią arytmetyczną elementów listy,
� zliczy, ile elementów jest mniejszych, a ile większych od średniej,
� wypisze na ekranie zawartość listy w odwrotnej kolejności (bez odwracania
samej listy).
Wszystkie wyznaczone wartości powinny zostać wyświetlone na ekranie."""
import random


def min_max(l: list) -> tuple:
    if len(l) == 0:
        print("list is empty, returning 0, 0")
        return 0, 0
    else:
        l_min = l[0]
        l_max = l[0]
        for i in l:
            if i < l_min:
                l_min = i
            if i > l_max:
                l_max = i
    return l_min, l_max


def list_info(l: list):
    print(l)
    print(f"min: {min_max(l)[0]}")
    print(f"max: {min_max(l)[1]}")
    print(f"avg: {sum(l) / len(l)}")
    print(f"less than avg: {sum([i in l for i in l if i < sum(l) / len(l)])}")
    print(f"more than avg: {sum([i in l for i in l if i > sum(l) / len(l)])}")
    print(f"{l[::-1]}")


l = [random.randint(-10, 10) for i in range(10)]
list_info(l)
