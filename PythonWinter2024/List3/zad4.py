"""Z zastosowaniem słowników napisać funkcję, której parametrem będzie zmienna
zawierająca łańcuch znaków. W funkcji należy policzyć częstość występowania
każdego znaku. Funkcja powinna zwrócić słownik zawierających wszystkie znaki
(jako klucze) i ich wystąpienia (wartość).
Przykładowo, dla:
liczZnaki(”Ala ma psa”)
powinien powstać słownik:
{’A’: 1, ’l’: 1, ’a’: 3, ’ ’: 2, ’m’: 1, ’p’: 1, ’s’: 1}"""


def letter_counter(s: str):
    res = {}
    for c in s:
        if c in res:
            res[c] += 1
        else:
            res[c] = 1

    print(res)


letter_counter("Ala ma kota")
