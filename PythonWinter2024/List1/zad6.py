"""Napisać program, który pobiera od użytkownika ciąg liczb całkowitych. Pobieranie

danych kończone jest podaniem wartości 0 (nie wliczana do danych). W następ-
nej kolejności program powinien wyświetlić sumę największej oraz najmniejszej

z podanych liczb oraz ich średnią arytmetyczną. Rozszerz zadanie, aby program
wyświetlał całą sekwencję liczb wprowadzonej przez użytkownika.
Przykład:
Użytkownik podał ciąg: 1, -4, 2, 17, 0.
Wynik programu:
13 // suma min. i maks.
6.5 // średnia"""


def min_max():
    u_input = input("Type a number (type 0 to stop): ")  # first input
    u_number = int(u_input)  # user input as int

    if u_number == 0:
        print("User input: 0")

    else:
        input_log = "" + u_input + ", "  # all numbers that user types
        u_min = u_number  # current min
        u_max = u_number  # current max

        # main loop
        while True:
            u_input = input("Type a number (type 0 to stop): ")
            u_num = int(u_input)

            # stop if user types 0
            if u_num == 0:
                input_log += u_input
                break

            input_log += u_input + ", "

            # check if min or max changed
            if u_num < u_min:
                u_min = u_num
            if u_num > u_max:
                u_max = u_num

        # printing results
        print(f"User input: {input_log}")
        print(f"Min: {u_min}")
        print(f"Max: {u_max}")
        print(f"Sum: {u_min+u_max}")
        print(f"Average: {(u_max + u_min) / 2:.2f}")


min_max()


