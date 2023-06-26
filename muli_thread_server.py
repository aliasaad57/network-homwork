import socket
import threading

questions = []

try:
    # Read the questions file
    with open('questions.txt', 'r') as file:
        for line in file:
            question, answer = line.strip().split(':')
            questions.append((question.strip(), answer.strip()))
except FileNotFoundError:
    print('Error: Questions file not found')
    exit()

# Define a function to start the server
host = '0.0.0.0'
port = 7474
def server():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen()
        print(f'Server listening on {host}:{port}')

        while True:
            client_socket, client_address = server_socket.accept()
            c_thread = threading.Thread(target=handle_quiz, args=(client_socket, client_address))
            c_thread.start()
    except socket.error:
        print('Error: Could not start the server')
    finally:
        server_socket.close()


def handle_quiz(client_socket, client_address):
    result = 0
    try:
        # Send the quiz questions to the client
        for question, answer in questions:
            client_socket.send(question.encode())
            client_answer = client_socket.recv(1024).decode().strip()
            
            if client_answer == answer:
                result += 1
        client_socket.send(f'Your score is {result} out of {len(questions)}.'.encode())
    except socket.error:
        print(f'Error: Could not handle quiz for client {client_address[0]}:{client_address[1]}')
    finally:
        client_socket.close()

if __name__ == '__main__':
    server()