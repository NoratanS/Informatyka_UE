"""Napisz program, w którym tworzona jest lista liczb nieparzystych z zakresu po-
danego przez użytkownika [a, b]. Użytkownik może podać dowolne wartości a oraz

b (można założyć, że są to liczby dodatnie). Program powinien:
� zadbać, aby lista zawierała tylko liczby nieparzyste. Przykładowo, dla a=5 i
b=10 lista powinna wynosić: [5,7,9], natomiast dla a=2 i b=9 lista: [3,5,7,9].
� zmodyfikować listę tak, aby każda liczba została zastąpiona krotką, w której
znajdują się: wartość liczby, 2 do potęgi tej liczby oraz pierwiastek z tej
liczby.
Przykładowy wynik:
Dla listy: [5,7,9]
wynik: [(5, 32, 2.23606797749979), (7, 128, 2.6457513110645907), (9, 512, 3.0)]"""

import math


def odd_list(a: int, b: int):
    num_list = [i for i in range(a, b + 1) if i % 2]
    res = [(x, 2 ** x, math.sqrt(x)) for x in num_list]
    print(res)


odd_list(5, 9)
