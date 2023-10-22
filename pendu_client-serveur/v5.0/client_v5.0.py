import socket

def main():
    host = socket.gethostname()
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print(client_socket.recv(1024).decode())  # Bienvenue au jeu du pendu !
    print("test1")

    niveau_choisi = input("Choisissez un niveau (facile, moyen, difficile) : ")
    print("test2")
    client_socket.send(niveau_choisi.encode())

    while True:
        print("test3")
        message = client_socket.recv(1024).decode()
        print(message)

        if "Fin de la partie" in message:
            break

        lettre_proposee = input("Proposez une lettre : ")
        client_socket.send(lettre_proposee.encode())
        print("test4")
    
    client_socket.close()

if __name__ == "__main__":
    main()