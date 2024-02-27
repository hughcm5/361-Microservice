import zmq
import time

def main():
    context = zmq.Context()

    print("Connecting to server")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    time.sleep(1.0)

    # Take user input for the number
    number = int(input("Enter a number: "))


    # Send the number to the microservice
    socket.send_string(str(number))

    # Receive and print the result
    result = int(socket.recv_string())
    print(f"Result: {result}")

    # Run until user closes terminal
    main()

if __name__ == "__main__":
    main()
