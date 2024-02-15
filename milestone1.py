about = "Caloric Balance Calculator (CBC) is a text-based application that calculates the difference between calories \n" \
        "calories consumed and calories burned in one day. Use your keyboard to enter numbers or select options as \n" \
        "prompted by the text. CBC will ask for your total calorie consumption for the day."

print("Welcome to Caloric Balance Calculator!\n")
while True:
    selection_1 = input(
        "Enter a number to select an option:\n"
        "\n    1. About Caloric Balance Calculator"
        "\n    2. Calculate Caloric Balance"
        "\n    3. Exit\n"
    )
    if selection_1 == "1":
        print(about)
    elif selection_1 == "2":
        selection_2 = input("Enter the total calories consumed today or ""z"" to cancel: ")
        if selection_2 == "z":
            pass
        elif selection_2.isdigit():
            balance = int(selection_2) - 1600  # simple calculation
            print(balance)
        else:
            print("Invalid input")
    elif selection_1 == "3":
        break
    else:
        print("Invalid input")



