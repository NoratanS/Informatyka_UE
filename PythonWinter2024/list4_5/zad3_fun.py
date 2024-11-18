"""3. Napisz funkcję obl wiel(x: float, n: int, *coeffs: float) -> float , któ-
ra oblicza wartość wielomianu stopnia n przy użyciu współczynników podanych

jako dodatkowe argumenty. Na przykład dla wielomianu 3x2 + 2x + 1 i x = 7
wywołanie funkcji powinno wyglądać następująco: obl wiel(7, 2, 1, 2, 3) .
Przykład:
print(obl_wiel(4, 2, 1, 2, 3)) # 57, bo 3 * 4^2 + 2 * 4 + 1 = 57
print(obl_wiel(3, 3, 5, -2, 0, 4)) # 98,

#bo 4 * 3^3 + 0 * 3^2 - 2 * 3 + 5 = 98"""
import math


def calculate_polynomial(x: float, n: int, *coeffs: float) -> float:
    if len(coeffs) != n + 1:
        raise ValueError("You need to specify n + 1 coefficients")

    coeffs_filled = [0] * (n + 1)
    for i in range(len(coeffs)):
        coeffs_filled[i] = coeffs[i]

    res = sum(coeffs_filled[i] * math.pow(x, i) for i in range(n + 1))
    return res


print(calculate_polynomial(4, 2, 1, 2, 3))
print(calculate_polynomial(3, 3, 5, -2, 0, 4))