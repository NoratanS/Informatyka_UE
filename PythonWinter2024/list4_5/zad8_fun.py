"""Napisz funkcję rekurencyjną, która symuluje przenoszenie dysków w problemie
wież Hanoi. Zadaniem jest przeniesienie wszystkich dysków z jednej wieży na

drugą przy użyciu trzeciej jako tymczasowej. Każdy krok powinien być wyświe-
tlany w konsoli, pokazując przeniesienie jednego dysku z jednej wieży na inną.

Przykładowe wywołanie:
hanoi(n, ’A’, ’C’, ’B’)
powinno wyświetlić kroki przenoszenia n dysków z wieży A na wieżę C przy
użyciu wieży B jako pomocniczej."""


def hanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    hanoi(n - 1, from_rod, aux_rod, to_rod)
    print("move disk ", n, " from ", from_rod, " to ", to_rod)
    hanoi(n - 1, aux_rod, to_rod, from_rod)


hanoi(5, "A", "C", "B")
