"""Napisz program, w którym przygotowane są dwie listy, pierwsz o wielkości n
(podanej przez użytkownka), druga o wielkości m (podanej przez użytkownika).
Następnie listy powinny być wypełnione wartościami losowymi z zakresu [1,10].
Wyświetl listę elementów, które występują w obu listach (czyli ich przecięcie).
Użyj zbiorów do rozwiązania tego problemu. (zbiory)"""
import random


def rand_intersect(n: int, m: int):
    l1 = [random.randint(1, 10) for i in range(n)]
    l2 = [random.randint(1, 10) for i in range(m)]
    print(f"{list(set(l1).intersection(set(l2)))}")


rand_intersect(10, 10)
