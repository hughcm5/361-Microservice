![alt text](https://github.com/hughcm5/361-Microservice/blob/main/UML.PNG "Logo Title Text 1)

The microserive can send two data inputs using Python ZMQ by encoding them as JSON data. After taking input from the user, you can follow these steps

1. Convert the two values you recieved from the user and put them into a list
2. Use socket.send_json() to send the list to the microservice as JSON data
3. On the server side, use socket.recv_data() to recieve the JSON data.
4. Take the first and second values of the list sent from the client side and store the values
5. Run the calculation.
6. Convert the calculation result into a string.
7. Send back the result using socket.send_string(result)
8. Back on the client side, recieve the data using the socket.recv_string() function and print the result. 
