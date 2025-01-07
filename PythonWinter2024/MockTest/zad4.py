class Punktacja:
    def __init__(self, waga=1, wartosc=0):
        if waga > 10 or waga < 1 or wartosc > 10 or wartosc < 0:
            raise ValueError("Wartosc musi byc z przedzialu (0, 10), waga z przedzialu (1, 10)")
        self.__waga = waga
        self.__wartosc = wartosc

    def __str__(self) -> str:
        return f"{self.__wartosc} punktów o wadze {self.__waga}"

    @property
    def waga(self) -> int:
        return self.__waga

    @waga.setter
    def waga(self, value):
        if not isinstance(value, int) or value < 1 or value > 10:
            raise ValueError("waga must be and integer between 1 and 10")
        self.__waga = value

    @property
    def wartosc(self):
        return self.__wartosc

    @wartosc.setter
    def wartosc(self, value):
        if not isinstance(value, int) or value < 0 or value > 10:
            raise ValueError("wartosc must be and integer between 1 and 10")
        self.__wartosc = value

    def __add__(self, other):
        new_waga = self.waga + other.waga
        new_wartosc = self.wartosc + other.wartosc
        if new_waga > 10:
            new_waga = 10
        if new_wartosc > 10:
            new_wartosc = 10
        return Punktacja(new_waga, new_wartosc)

    def __mul__(self, other):
        new_waga = (self.waga + other.waga) // 2
        new_wartosc = (self.wartosc + other.wartosc) // 2
        return Punktacja(new_waga, new_wartosc)

    def koncowa(self):
        return self.__waga * self.__wartosc


class Produkt:
    def __init__(self, nazwa: str, punkty: Punktacja, dodatkowe_punkty: int):
        self.__nazwa = nazwa
        self.__punkty = punkty
        self.__dodatkowe_punkty = dodatkowe_punkty

    def __gt__(self, other):
        return self.__dodatkowe_punkty + self.__punkty.koncowa() > other.__dodatkowe_punkty + other.__punkty.koncowa()


punkt1 = Punktacja(2,8)
punkt2 = Punktacja(1,4)
produkt = Produkt("Klawiatura A", punkt1, 20)
produkt2 = Produkt("Monitor C", punkt2, 33)

print(produkt > produkt2)
print(produkt2 > produkt)
