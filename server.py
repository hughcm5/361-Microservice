import zmq

def calculate(number):
    return 1600 - number  # Average base metabolic rate

def main():
    context = zmq.Context()

    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")  

    print("Server running") # Check if server is running

    while True:
        # Recieves the number
        number = int(socket.recv_string())

        # Run calculate function
        result = calculate(number)

        # Send back to client
        socket.send_string(str(result))

if __name__ == "__main__":
    main()
