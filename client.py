import zmq
import time
import json

def main():
    context = zmq.Context()

    print("Connecting to server")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    while True:
        # Take user input for the number
        cals = int(input("Enter number of calories consumed: "))
        activity = input("Enter activity level(sedentary, light, moderate, or active): ")

        cals = str(cals)
        lst = [activity,cals]
        encoded_lst = json.dumps(lst)

        # Send the number to the microservice
        socket.send_json(encoded_lst)

        # Receive and print the result
        result = socket.recv_string()

        print(f"Result: {result}")


if __name__ == "__main__":
    main()
