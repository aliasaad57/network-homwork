import socket

try:
    client_socket = socket.socket()
    client_socket.connect(('127.0.0.1', 7474))

    while True:
        try:
            question = client_socket.recv(1024).decode()
            if not question:
                break
            # Send the answer to the server
            answer = input(question + ' ')
            client_socket.send(answer.encode())
        except socket.error:
            print('Error')
            break

    # Receive the final score from the server
    try:
        score = client_socket.recv(1024).decode()
        print(score)
    except socket.error:
        print('Error: Could not receive the final score from the server')
except ConnectionRefusedError:
    print('Error: Could not connect to the server. Please check that it is running and try again.')
finally:
    # Close the client socket
    client_socket.close()