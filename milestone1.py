import zmq

context = zmq.Context()

print("connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

about = "Caloric Balance Calculator (CBC) is a text-based program that calculates the difference between calories\n" \
    "calories consumed and calories burned in one day. Use your keyboard to enter numbers or select options as \n" \
    "prompted by the text. CBC will ask for your total calorie consumption for the day. Maintain a negative \n" \
    "balance to effect weight loss and a positive balance for weight gain.\n"

print("Welcome to Caloric Balance Calculator!\n")
while True:
    selection_1 = input(
        "Enter a number to select an option:\n"
        "\n    1. About Caloric Balance Calculator (25 second read)"
        "\n    2. Calculate Caloric Balance"
        "\n    3. Exit\n"
    )
    if selection_1 == "1":
        print(about)
    elif selection_1 == "2":
        selection_2 = input("Enter the total calories consumed today or \"z\" to cancel: ")
        if selection_2 == "z":
            pass
        elif selection_2.isdigit():
            selection_3 = input(
                "What is your activity level? Enter a number:\n"
                "\n    1. Sedentary"
                "\n    2. Light"
                "\n    3. Moderate\n"
                "\n    4. Active\n"
            )
            if selection_3 == "1":
                selection_3 = "sedentary"
            elif selection_3 == "2":
                selection_3 = "light"
            elif selection_3 == "3":
                selection_3 = "moderate"
            elif selection_3 == "4":
                selection_3 = "active"
            else:
                break
            list_request = [selection_2, selection_3]
            socket.send_json(list_request)
            balance = socket.recv_string()
            print(balance)
        else:
            print("Invalid input")
    elif selection_1 == "3":
        break
    else:
        print("Invalid input")
