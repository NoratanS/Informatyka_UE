"""Napisz program, w którym wczytywany jest ciąg słów (każde słowo, jako kolejny

element listy). Następnie, używając zbiorów i słowników, oblicz częstość wystę-
powania każdego słowa w tym ciągu. (zbiory)"""


def word_frequency(words: []):
    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1

    print(frequencies)


word_frequency(['cat', 'dog', 'rabbit', 'cat'])
