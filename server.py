import zmq

def calculate(number):
    return 1600 - number

def main():
    # Create a ZeroMQ context
    context = zmq.Context()

    # Create a socket to receive messages
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")  # Binding to TCP port 5555

    print("Server running")

    while True:
        # Recieves the number
        number = int(socket.recv_string())

        # Subtract
        result = calculate(number)

        # Send back to client
        socket.send_string(str(result))

if __name__ == "__main__":
    main()
