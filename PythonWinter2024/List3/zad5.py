def liczba_na_slowa(liczba):
    #TODO po swojemu
    jednostki = {
        0: "zero", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery",
        5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem", 9: "dziewięć"
    }

    nastki = {
        10: "dziesięć", 11: "jedenaście", 12: "dwanaście", 13: "trzynaście",
        14: "czternaście", 15: "piętnaście", 16: "szesnaście",
        17: "siedemnaście", 18: "osiemnaście", 19: "dziewiętnaście"
    }

    dziesiatki = {
        20: "dwadzieścia", 30: "trzydzieści", 40: "czterdzieści",
        50: "pięćdziesiąt", 60: "sześćdziesiąt", 70: "siedemdziesiąt",
        80: "osiemdziesiąt", 90: "dziewięćdziesiąt"
    }

    setki = {
        100: "sto", 200: "dwieście", 300: "trzysta", 400: "czterysta",
        500: "pięćset", 600: "sześćset", 700: "siedemset", 800: "osiemset",
        900: "dziewięćset"
    }

    tysiac = "tysiąc"
    tysiące = ["tysiące", "tysięcy"]

    def trzy_cyfry(n):
        """Funkcja pomocnicza do tłumaczenia liczb 0–999."""
        if n == 0:
            return ""

        wynik = ""

        # Setki
        if n >= 100:
            setka = (n // 100) * 100
            wynik += setki[setka] + " "
            n %= 100

        # Nastki (10-19)
        if 10 <= n <= 19:
            wynik += nastki[n]
            return wynik.strip()

        # Dziesiątki
        if n >= 20:
            dziesiatka = (n // 10) * 10
            wynik += dziesiatki[dziesiatka] + " "
            n %= 10

        # Jednostki
        if n > 0:
            wynik += jednostki[n]

        return wynik.strip()

    if liczba == 0:
        return jednostki[0]

    wynik = ""

    # Tysiące
    if liczba >= 1000:
        tys = liczba // 1000
        if tys == 1:
            wynik += tysiac + " "
        elif 2 <= tys <= 4:
            wynik += trzy_cyfry(tys) + " " + tysiące[0] + " "
        else:
            wynik += trzy_cyfry(tys) + " " + tysiące[1] + " "
        liczba %= 1000

    # Setki, dziesiątki i jednostki
    wynik += trzy_cyfry(liczba)

    return wynik.strip()


# Przykład użycia
print(liczba_na_slowa(234567))  # "dwieście trzydzieści cztery tysiące pięćset sześćdziesiąt siedem"
print(liczba_na_slowa(1001))  # "tysiąc jeden"
print(liczba_na_slowa(450000))  # "czterysta pięćdziesiąt tysięcy"
print(liczba_na_slowa(999999))  # "dziewięćset dziewięćdziesiąt dziewięć tysięcy dziewięćset dziewięćdziesiąt dziewięć"
