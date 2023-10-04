import socket

def main():
    host = socket.gethostname() 
    port = 1234

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        message = client_socket.recv(1024).decode()
        print(message)

        if "Bravo" in message or "Dommage" in message:
            break

        lettre_proposee = input("Proposez une lettre ou un mot : ").lower()
        client_socket.send(lettre_proposee.encode())

    client_socket.close()

if __name__ == "__main__":
    main()
