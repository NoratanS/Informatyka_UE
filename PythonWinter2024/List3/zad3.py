"""Stwórz listę 20 losowych wartości z zakresu [0,10]. Następnie (przy zastosowaniu
zbiorów) wyświetl listę wszystkich podzbiorów wartości tych liczb. (zbiory)"""
import math
import random


def power_set(nums: []):
    """We use bit representation to determine what elements will be in a subset
    for set {1,2,3,4} a subset {1,2} would be 0011"""
    num_set = list(set(nums))
    print(num_set)

    set_size = len(num_set)
    power_set_size = int(math.pow(2, set_size))

    res = []
    for counter in range(power_set_size):
        aux = set()
        for j in range(set_size):
            # we check if jth bit in counter is 1, if so we add element to subset
            # 1 << 2 for example is 100, if counter is 1100 we will add the [j] element
            if (counter & (1 << j)) > 0:
                aux.add(num_set[j])
        res.append(aux)

    print(res)


l1 = [random.randint(0, 40) for _ in range(100)]
power_set(l1)


