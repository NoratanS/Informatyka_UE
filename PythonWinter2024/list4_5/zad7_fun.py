"""7. Napisz funkcję polacz(lst1: list[int], lst2: list[int], lst3: list[int]) ,
która łączy elementy dwóch list lst1 i lst2 naprzemiennie do trzeciej listy
lst3 .
Przykład użycia:
lst1 = [0, 1, 2, 3, 4, 5, 6, 7]
lst2 = [10, 11, 12, 13, 14]
lst3 = []
polacz(lst1, lst2, lst3)
print(lst3) # [0, 10, 1, 11, 2, 12, 3, 13, 4, 14, 5, 6, 7]"""


def concat(lst1: list[int], lst2: list[int]) -> list[int]:
    lst3 = []
    i = 0
    j = 0

    while i < len(lst1) and j < len(lst2):
        lst3.append(lst1[i])
        lst3.append(lst2[j])
        i += 1
        j += 1

    if i == len(lst1):
        while j < len(lst2):
            lst3.append(lst1[j])
            j += 1
    else:
        while i < len(lst1):
            lst3.append(lst1[i])
            i += 1

    return lst3


lst1 = [0, 1, 2, 3, 4, 5, 6, 7]
lst2 = [10, 11, 12, 13, 14]
lst3 = []
print(concat(lst1, lst2))
