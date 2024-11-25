"""Bez metod z str zdefiniuj funkcję

strcut(text: str, start: int, length: int) -> str , która wycina z po-
danego łańcucha text fragment zaczynający się od indeksu start o długości

length . Funkcja zwraca wycięty fragment.
Przykłady:
print(strcut("Ala ma kota", 1, 2)) # Oczekiwany wynik: "la"
print(strcut("Ala ma kota", 5, 4)) # Oczekiwany wynik: "a ko"""


def strcut(text: str, start: int, length: int) -> str:
    return text[start:start + length]


print(strcut("Ala ma kota", 1, 2))
print(strcut("Ala ma kota", 5, 4))