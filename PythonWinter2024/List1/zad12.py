"""Napisać program, który implementuje algorytm Euklidesa do znalezienia największego wspólnego dzielnika (NWD) dwóch liczb oraz rozszerzony algorytm Euklidesa do znalezienia współczynników wyrażenia Bezouta dla tych liczb. Program
powinien wyświetlać pełny przebieg obliczeń, aby użytkownik mógł zrozumieć,
jak działają kolejne kroki algorytmu."""


def gcd_recursive(a: int, b: int) -> int:
    print(f"{a}, {b}")
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)


def gcd_iterative(a: int, b: int) -> int:
    while b != 0:
        print(f"{a} {b}")
        c = a % b
        a = b
        b = c
    print(a)
    return a


print(f"gcd(42,12) = {gcd_recursive(42, 12)}")
print()
print(f"gcd(122, 42) = {gcd_iterative(122, 42)})")

# TODO: extended euclidean