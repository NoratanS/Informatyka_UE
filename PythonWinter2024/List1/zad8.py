"""8. Napisać program, który pobiera od użytkownika liczbę całkowitą, a następnie:
� oblicza sumę cyfr tej liczby,
� stosunek średniej arytmetycznej cyfr parzystych do średniej arytmetycznej
cyfr nieparzystych.
Dodaj walidację, aby użytkownik nie mógł podać liczby ujemnej oraz możliwość
wprowadzenia dodatkowej liczby i wyliczenia stosunku sum cyfr obu liczb."""


def digit_sum_input():
    num = input("Type a positive number: ")
    if int(num) <= 0:
        print("Only positive numbers are allowed")
        return digit_sum_input()
    else:
        return int(num)


# mod - modulo (1 for all numbers), which - are dividable (True) not dividable (False)
def digit_sum(num: int, mod: int, which: bool):
    res = 0
    while num > 0:
        d = num % 10
        if (d % mod == 0) == which:  # is it dividable? == do we want it to be?
            res += d
        num //= 10
    return res


# mod - modulo (1 for all numbers), which - are dividable (True) not dividable (False)
def digit_count(num: int, mod: int, which: bool):
    res = 0
    while num > 0:
        d = num % 10
        if (d % mod == 0) == which:  # is it dividable? == do we want it to be?
            res += 1
        num //= 10
    return res


# mod - modulo (1 for all numbers), which - are dividable (True) not dividable (False)
def digit_average(num: int, mod: int, which: bool):
    if digit_count(num, mod, which) == 0:  # If there are no digits that match the condition return -1
        return -1
    else:
        return digit_sum(num, mod, which) / digit_count(num, mod, which)


def digit_info():
    # first input
    u_num1 = digit_sum_input()

    # calculations for first number
    num1_even_sum = digit_sum(u_num1, 2, True)
    num1_odd_sum = digit_sum(u_num1, 2, False)

    # printing first number results
    print(f"Digit sum: {num1_even_sum + num1_odd_sum}")
    print(f"Even average to odd average aatio\n" +
          f"{digit_average(u_num1, 2, True):.2f} : " +
          f"{digit_average(u_num1, 2, False):.2f}")

    # second number
    u_option = input("Do you want to add another number? 1 if yes")
    if u_option == "1":
        u_num2 = digit_sum_input()
        print(f"First and second number digit sum ratio:\n" +
              f"{num1_even_sum + num1_odd_sum} : " +
              f"{digit_sum(u_num2, 1, True)}")


digit_info()
