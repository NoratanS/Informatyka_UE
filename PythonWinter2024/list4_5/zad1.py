"""1. Napisać program, który wczytuje od użytkownika ciąg znaków, a następnie wyświetla informację o tym ile razy w tym ciągu powtarza się jego ostatni znak.
Przykład, dla ciągu „Abrakadabra” program powinien wyświetlić 4, ponieważ
ostatnim znakiem jest literka „a”, która występuje w podanym ciągu łącznie 4
razy.
W celu treningu warto wykonać zadanie z zastosowaniem metody string.count()
oraz bez tej metody. ."""


def count_last_char(s: str):
    print(s.count(s[len(s) - 1]))


def count_last_char2(s: str):
    c = s[len(s) - 1]
    res = 0
    for char in s:
        if char == c:
            res += 1
    print(res)


count_last_char("Abrakadabra")
count_last_char2("Abrakadabra")
