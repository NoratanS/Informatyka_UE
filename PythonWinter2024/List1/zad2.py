def CalcInstalment():
    # Inputs
    price = float(input("Type the price [pln]: "))
    months = int(input("How many instalments: "))

    # Check Inputs
    if 100 > price > 10000:
        print("Incorrect price")
        CalcInstalment()

    if 6 > months > 48:
        print("Incorrect months")
        CalcInstalment()

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


CalcInstalment()
