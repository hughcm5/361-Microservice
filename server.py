import zmq
import json


def calculate(activity, cals):
    bmr = 1600

    if activity == 'sedentary':
        activity = 350
    elif activity == 'light':
        activity = 700
    elif activity == 'moderate':
        activity = 850
    elif activity == 'active':
        activity = 1000

    return cals - bmr - activity

def main():
    context = zmq.Context()

    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")  

    print("Server running") # Check if server is running

    while True:
        # Receive data from client
        data = socket.recv_json()
        print(data)

        activity = data[0]
        cals = data[1]

        # Run calculate function
        result = calculate(activity, cals)

        result = str(result)

        # Send back to client
        socket.send_string(result)

if __name__ == "__main__":
    main()
