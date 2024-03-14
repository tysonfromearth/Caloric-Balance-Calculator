import zmq

context = zmq.Context()

print("connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

about = "Caloric Balance Calculator (CBC) is a text-based program that calculates the difference between\n" \
    "calories consumed and calories burned in one day. Use your keyboard to enter numbers or select\n" \
    "options as prompted by the text. CBC will ask for your total calorie consumption for the day \n" \
    "and your activity level. Maintain a negative balance to effect weight loss and a positive balance\n" \
    "for weight gain."

print("Welcome to Caloric Balance Calculator!\n")


def use_microservice(list_request):
    socket.send_json(list_request)
    balance = socket.recv_string()
    print(balance)


def activity_converter(selection_3):
    if selection_3 == "1":
        return "sedentary"
    elif selection_3 == "2":
        return "light"
    elif selection_3 == "3":
        return "moderate"
    elif selection_3 == "4":
        return "active"
    else:
        print("Invalid input")


def get_input():
    while True:
        selection_2 = input("Enter the total calories consumed today or \"z\" to cancel: ")
        if selection_2 == "z":
            return "home screen"
        elif selection_2.isdigit():
            selection_3 = input(
                "What is your activity level? Enter a number:\n"
                "\n    1. Sedentary"
                "\n    2. Light"
                "\n    3. Moderate"
                "\n    4. Active\n"
            )
            selection_3 = activity_converter(selection_3)
            return [selection_2, selection_3]
        else:
            print("Invalid input")


def home_screen():
    selection_1 = input(
        "Enter a number to select an option:\n"
        "\n    1. About Caloric Balance Calculator (25 second read)"
        "\n    2. Calculate Caloric Balance"
        "\n    3. Exit\n"
    )
    if selection_1 == "1":
        print(about)
    elif selection_1 == "2":
        list_request = get_input()
        if list_request == "home screen":
            pass
        else:
            use_microservice(list_request)
    elif selection_1 == "3":
        return "exit"
    else:
        print("Invalid input")


while True:
    if home_screen() == "exit":
        break
