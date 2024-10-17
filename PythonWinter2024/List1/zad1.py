def CalcBmi():
    weight = float(input("Type your weight [kg]: "))
    height = float(input("Type your height [m]: "))

    # Check if inputs are valid
    if weight < 0 or height < 0:
        print("You must enter a valid height.")
        CalcBmi()

    # Calculate bmi
    bmi = weight / (height * height)

    # Logic and printing
    if 18.5 <= bmi < 25:
        print(f"BMI: {bmi:.2f}  Waga prawidłowa")
    elif bmi < 18.5:
        print(f"BMI: {bmi:.2f}  Niedowaga")
    else:
        print(f"BMI: {bmi:.2f}  Nadwaga")

CalcBmi()