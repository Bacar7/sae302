import socket

def main():
    host = socket.gethostname()
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print(client_socket.recv(1024).decode())

    niveau_choisi = input("Choisissez un niveau (facile, moyen, difficile) : ")
    client_socket.send(niveau_choisi.encode())

    while True:
        message = client_socket.recv(1024).decode()
        print(message)

        if "Fin de la partie" in message:
            break

        if "Bravo" in message :
            message = client_socket.recv(1024).decode()
            print(message)
            break

        if "Perdu" in message :
            message = client_socket.recv(1024).decode()
            print(message)
            break

        lettre_proposee = input("Proposez une lettre : ")
        client_socket.send(lettre_proposee.encode())

    client_socket.close()

if __name__ == "__main__":
    main()