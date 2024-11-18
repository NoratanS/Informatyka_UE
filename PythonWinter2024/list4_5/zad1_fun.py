"""Zdefiniuj funkcję min value(lst: list[float]) -> float , która znajduje i
zwraca minimalną wartość w liście lst .

Następnie zdefiniuj funkcję max value(lst: list[float], wynik: list) , któ-
ra znajduje maksymalną wartość w liście lst i zwraca ją przez opcjonalny pa-
rametr wynik . Wynik powinien być przypisany do wynik[0] .

Przykład:
lst = [4.5, 1.2, 8.3]
max_v = [0]
min_v = min_value(lst)
max_value(lst, wynik)
print(min_v, max_v[0]) #1.2 8.3"""


def min_value(lst: list[float]) -> float:
    res = lst[0]
    for i in lst:
        if i < res:
            res = i
    return res


def max_value(lst: list[float], result: list):
    res = lst[0]
    for i in lst:
        if i > res:
            res = i
    result[0] = res


lst = [4.5, 1.2, 8.3]
max_v = [0]
min_v = min_value(lst)
max_value(lst, max_v)
print(min_v, max_v[0])
