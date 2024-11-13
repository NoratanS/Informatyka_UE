"""W języku HTML oraz kaskadowych arkuszach stylów (CSS) powszechne jest usta-
lanie kolorów elementów w postaci łańcucha #RRGGBB, gdzie RR jest dwucyfrową

liczbą (od 0x0 do 0xFF) w kodzie szesnastkowym oznaczającą ile czerwieni jest

w wynikowym kolorze. Analogicznie GG oznacza nasycenie zieleni, a BB niebie-
skiego.

Napisać funkcję html to rgb(color) , która jako parametr przyjmuje łańcuch

postaci ”#RRGGBB” i zwraca tablicę 3 liczb całkowitych w systemie 10 ozna-
czających nasycenie poszczególnych składowych.

Przykład

9

Wynikiem html_to_rgb("#FF0050") powinna być krotka (255, 0, 80).
Wynikiem html_to_rgb("#001020") powinna być krotka (0, 16, 32)."""


def html_to_rgb(color: str):
    r = int(color[1:3], 16)
    g = int(color[3:5], 16)
    b = int(color[5:], 16)
    return r, g, b


print(html_to_rgb("#FF0050"))
print(html_to_rgb("#001020"))

