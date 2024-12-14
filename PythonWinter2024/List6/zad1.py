"""1. Napisać funkcję def szukaj(nazwaPlikWe, nazwaPlikWy, slowo) , której za-
daniem jest znalezienie wszystkich wierszy w pliku, które zawierają szukane sło-
wo. Wszystkie wiersze, które zawierają słowo powinny zostać zapisane w pliku

wynikowym wraz z nr wiersza (z pierwszego pliku). Nazwa pierwszego pliku za-
pamiętana jest w parametrze nazwaPlikWe, nazwa pliku wynikowego podana jest

w parametrze nazwaPlikWy, natomiast szukane słowo w parametrze slowo.
Przykład - plik wejściowy:
Ala ma jutro egzamin z biologii.
Jan myje auto.
Eh, jutro kolejny egzamin.
Nie lubie polityki.
Jeżeli szukanym słowem byłoby ”egzamin”, to plik wynikowy powinien wyglądać
następująco:
1: Ala ma jutro egzamin z biologii.
3: Eh, jutro kolejny egzamin."""


def find_matches(filename: str, result_file: str, pattern: str) -> None:
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    result_file = open(result_file, "w")
    for i in range(len(lines)):
        if pattern in lines[i]:
            result_file.write(f"{i + 1}: {lines[i]}")
    result_file.close()


find_matches("zad1_data.txt", "zad1_result.txt", "egzamin")
