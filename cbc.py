import zmq
from playsound import playsound

# connect to the server
context = zmq.Context()
print("connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# initialize variables
greeting = "Welcome to Caloric Balance Calculator!"
input1 = "Enter a number to select an option:\n" \
         "\n    1. About Caloric Balance Calculator (25 second read)" \
         "\n    2. Calculate Caloric Balance" \
         "\n    3. Exit\n"
about = "Caloric Balance Calculator (CBC) is a text-based program that calculates the difference between\n" \
        "calories consumed and calories burned in one day. Use your keyboard to enter numbers or select\n" \
        "options as prompted by the text. CBC will ask for your total calorie consumption for the day \n" \
        "and your activity level. Maintain a negative balance to effect weight loss and a positive balance\n" \
        "for weight gain."
input2 = "Enter the total calories consumed today or \"z\" to cancel: "
input3 = "What is your activity level? Enter a number:\n" \
         "\n    1. Sedentary" \
         "\n    2. Light" \
         "\n    3. Moderate" \
         "\n    4. Active\n"
goodbye = "Thanks for using Caloric Balance Calculator, goodbye!"


def use_microservice(list_request):
    """Sends user-provided list to microservice then receives and prints the result."""
    socket.send_json(list_request)
    balance = socket.recv_string()
    print(balance)


def activity_converter(selection_3):
    """Converts user-input number to the corresponding string for microservice communication."""
    if selection_3 == "1":
        return "sedentary"
    elif selection_3 == "2":
        return "light"
    elif selection_3 == "3":
        return "moderate"
    elif selection_3 == "4":
        return "active"
    else:
        return 'Invalid input'


def get_input():
    """Gathers user's calories consumed and activity level then returns them as a list in that order."""
    while True:
        selection_2 = input(input2)
        if selection_2 == "z":
            return "home screen"  # home_screen() function checks for this to return to initial menu
        elif selection_2.isdigit() and int(selection_2) >= 0:
            selection_3 = input(input3)
            if selection_3.isdigit() and 1 <= int(selection_3) <= 4:
                selection_3 = activity_converter(selection_3)  # converts from a number to a corresponding string
                return [selection_2, selection_3]
            else:
                print('Invalid input')
        else:
            print("Invalid input")


def home_screen():
    """Gathers user input to navigate the application and use a microservice that calculates caloric balance."""
    selection_1 = input(input1)
    if selection_1 == "1":
        print(about)
        playsound('./about.mp3')
    elif selection_1 == "2":
        list_request = get_input()
        if list_request == "home screen":  # loops user back to initial selection screen
            pass
        else:
            use_microservice(list_request)
    elif selection_1 == "3":
        socket.send_string('exit')
        return "exit"
    else:
        print("Invalid input")


def main():

    print(greeting)
    while True:
        if home_screen() == "exit":
            break
    print(goodbye)


if __name__ == "__main__":
    main()
