"""Napisać program, który oblicza wartość współczynnika BMI (ang. body mass
index) wg. wzoru: waga

wzrost2 . Jeżeli wynik jest w przedziale (18,5 - 24,9) to wypisu-
je ”waga prawidłowa”, jeżeli poniżej to ”niedowaga”, jeżeli powyżej ”nadwaga”.

Program powinien sprawdzić, czy podane dane są dodatnie. W przypadku nie-
prawidłowych danych, program powinien poinformować użytkownika i poprosić o

ponowne wprowadzenie."""


def calc_bmi():
    # Inputs
    weight = float(input("Type your weight [kg]: "))
    height = float(input("Type your height [m]: "))

    # Check if inputs are valid
    if weight < 0 or height < 0:
        print("You must enter a valid height.")
        calc_bmi()

    # Calculate bmi
    bmi = weight / (height * height)

    # Logic and printing
    if 18.5 <= bmi < 25:
        print(f"BMI: {bmi:.2f}  Waga prawidłowa")
    elif bmi < 18.5:
        print(f"BMI: {bmi:.2f}  Niedowaga")
    else:
        print(f"BMI: {bmi:.2f}  Nadwaga")


calc_bmi()
