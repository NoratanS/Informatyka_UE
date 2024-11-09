"""Napisać program, który sumuje cyfry w tekście podanym przez użytkownika.
Przykład:
"Ala ma 1 psa i 2 koty. Jola ma 10 rybek i 2 papugi."
Wynik:
6"""


def count_digits(s: str) -> int:
    res = 0
    for c in s:
        if c.isdigit():
            res += int(c)
    return res


print(count_digits("Ala ma 1 psa i 2 koty. Jola ma 10 rybek i 2 papugi."))
