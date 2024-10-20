"""W sklepie ze sprzętem AGD oferowana jest sprzedaż ratalna. Napisz program
umożliwiający wyliczenie wysokości miesięcznej raty za zakupiony sprzęt. Danymi
wejściowymi dla programu są:
� cena towaru (od 100 zł do 10 tyś. zł),
� liczba rat (od 6 do 48).
Kredyt jest oprocentowany w zależności od liczby rat:
� od 6–12 wynosi 2.5% ,
� od 13–24 wynosi 5%,
� od 25–48 wynosi 10%.
Obliczona miesięczna rata powinna zawierać również odsetki. Program powinien
sprawdzać, czy podane dane mieszczą się w określonych powyżej zakresach, a w
przypadku błędu prosić użytkownika ponownie o podanie danych. Sposób liczenia
odsetek może być najprostszy (od aktualnej kwoty zadłużenia)."""


def calc_instalment():
    # Inputs
    price = float(input("Type the price [pln]: "))
    months = int(input("How many instalments: "))

    # Check Inputs
    if 100 > price > 10000:
        print("Incorrect price")
        calc_instalment()

    if 6 > months > 48:
        print("Incorrect months")
        calc_instalment()

    # Initializing rate
    rate = 0

    # Rate Logic
    if months <= 12:
        rate = 0.025
    elif months <= 24:
        rate = 0.05
    else:
        rate = 0.1

    # calculate instalment
    instalment = (price + price * rate) / months
    print(f"Your instalment is {instalment:.2f}")


calc_instalment()

