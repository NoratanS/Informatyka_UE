"""Napisać program, który wczytuje liczby podawane przez użytkownika dotąd, do-
póki nie podana zostanie liczba 0. Następnie wyświetlić sumę wszystkich poda-
nych liczb."""

def UserSum():
    # here we store our current sum
    sum = 0

    # user input var
    num = int(input("Type a Number (type 0 to stop): "))

    # main loop
    while num != 0:
        sum += num
        num = int(input("Type a Number: "))

    # printing result
    print(f"Your total is {sum}")

UserSum()