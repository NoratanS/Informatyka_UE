"""Gra w ”Za dużo, za mało”. Komputer losuje liczbę z zakresu 1 . . . 100, a gracz
(użytkownik) ma za zadanie odgadnąć, co to za liczba poprzez podawanie kolejnych wartości. Jeżeli podana wartość jest:
� większa – wyświetlany jest komunikat „Podałeś za dużą wartość”,
� mniejsza – wyświetlany jest komunikat „Podałeś za małą wartość”,
� identyczna z wylosowaną – wyświetlany jest komunikat „Gratulacje” i gra
się kończy.
Rozszerz zadanie, dodając licznik prób oraz możliwość wyboru poziomu trudności
(zakresy 1-50, 1-100, 1-200)."""

import random


def game():
    u_input = input("Choose difficulty:\n 1 for easy (1-50)\n 2 for medium (1-100)\n 3 for hard (1-200)\n")
    u_num = int(u_input)  # user input as int

    # choosing difficulty
    if u_num != 1 and u_num != 2 and u_num != 3:
        print("Invalid difficulty")
        game()

    # setting game range
    game_range: int
    if u_num == 1:
        game_range = 50
    elif u_num == 2:
        game_range = 100
    else:
        game_range = 200

    # selecting number to be guessed
    answer = random.randint(1, game_range)

    # game loop
    turn_count = 0
    while True:
        u_num = int(input("Your guess: "))
        turn_count += 1

        # Check for win
        if u_num == answer:
            print(f"Correct! It only took you {turn_count} guesses")
            break

        # Provide a hint
        elif u_num > answer:
            print("Your guess is too high")
        else:
            print("Your guess is too low")


game()
