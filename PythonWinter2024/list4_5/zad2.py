"""2. Napisać program, który wczytuje od użytkownika ciąg znaków, a następnie sprawdza, czy podany ciąg jest palindromem. Proszę spróbować zadbać o efektywność
tego rozwiązania."""


def is_palindrome(word: str) -> bool:
    word = "".join(word.lower().split())
    return word == word[::-1]


print(is_palindrome("A to kawa kota"))
