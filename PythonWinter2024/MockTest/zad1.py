def my_sort(lst: list[list]) -> list[list[list]]:
    res = []
    for i in range(len(lst[0])):
        res.append(sorted(lst, key=lambda x: x[i]))
    return res


print(my_sort([[1, 2, 3], [2, 5, 1], [3, 1, 2]]))
