class Rzecz:
    def __init__(self, waga=1, wartosc=0):
        self.waga = waga
        self.wartosc = wartosc

    def __str__(self) -> str:
        return f"Rzecz(waga={self.waga}, wartosc={self.wartosc})"

    @property
    def waga(self) -> int:
        return self.__waga

    @waga.setter
    def waga(self, value):
        if isinstance(value, int) and 1 <= value <= 10:
            self.__waga = value
        else:
            raise ValueError("waga must be and integer between 1 and 10")

    @property
    def wartosc(self):
        return self.__wartosc

    @wartosc.setter
    def wartosc(self, value):
        if isinstance(value, int) and 0 <= value <= 10:
            self.__wartosc = value
        else:
            raise ValueError("wartosc must be and integer between 0 and 10")

    def __add__(self, other):
        return Rzecz(min(10, self.waga + other.waga), min(10, self.wartosc + other.wartosc))

    def __mul__(self, other):
        return Rzecz((self.waga + other.waga) // 2, (self.wartosc + other.wartosc) // 2)

    def __gt__(self, other):
        return self.final_value() > other.final_value()

    def final_value(self):
        return self.waga * self.wartosc


r1 = Rzecz(2, 8)
r2 = Rzecz(3, 4)
print(r1)
print(r1.final_value())
print(r2.final_value())
print(r1 > r2)
r3 = r1 + r2
print(r3)
r4 = r1 * r2
print(r4)
