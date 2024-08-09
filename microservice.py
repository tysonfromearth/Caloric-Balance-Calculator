import zmq


def calculate(activity, cals):
    """
    Calculate calories burned
    """
    bmr = 1600
    activity_calories = 0

    if activity == 'sedentary':
        activity_calories = 350
    elif activity == 'light':
        activity_calories = 700
    elif activity == 'moderate':
        activity_calories = 850
    elif activity == 'active':
        activity_calories = 1000
    return int(cals) - bmr - activity_calories


def main():
    context = zmq.Context()

    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print("Server running")  # Check if server is running

    while True:
        # check if exit
        exit_string = socket.recv_string()
        if exit_string == "exit":
            break

        # Receive data from client
        data = socket.recv_json()

        # Get first and second items of list
        cals = data[0]
        activity = data[1]

        # Run calculate function
        result = calculate(activity, cals)

        # Convert result to string
        result_str = str(result)

        # Send back to client
        socket.send_string(result_str)


if __name__ == "__main__":
    main()
