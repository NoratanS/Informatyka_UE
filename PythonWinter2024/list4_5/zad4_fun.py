"""Bez metod z str zdefiniuj funkcję strpos(text: str, z: str) -> int , która
zwraca indeks, na którym znajduje się znak z w podanym łańcuchu text . Jeśli
znak z nie występuje w łańcuchu, funkcja powinna zwrócić -1.
Przykład użycia:
print(strpos("Ala ma kota", "a")) # Oczekiwany wynik: 1
print(strpos("Ala ma kota", "z")) # Oczekiwany wynik: -1"""


def strpos(text: str, z: str) -> int:
    for i in range(len(text)):
        if text[i] == z:
            return i
    return -1


print(strpos("Ala ma kota", "a"))
print(strpos("Ala ma kota", "z"))
