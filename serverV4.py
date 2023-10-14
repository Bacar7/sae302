import socket
import threading #contient des fonctionnalités pour travailler avec 
#des threads. permet de créer et de gérer des threads, 
#utils pour exécuter plusieurs parties d'un programme simultanément.
import random

# Variables
clients = 0
 

def choisir_niveau(niveau):
    mots_faciles = ["moto", "avion", "chat", "camion", "lapin", "chien"]
    mots_moyens = ["ordinateur", "programmation", "éléphant", "intelligence", "algorithme"]
    mots_difficiles = ["rhinopharyngitolaryngographologiquement", "cyclopentanoperhydrophénanthrène", "hippopotomonstrosesquippedaliophobie"]

    if niveau == "facile":
        return random.choice(mots_faciles)
    elif niveau == "moyen":
        return random.choice(mots_moyens)
    elif niveau == "difficile":
        return random.choice(mots_difficiles)

def jeu_pendu(mySocket):
    
    niveaux = ["facile", "moyen", "difficile"]
    mySocket.send("\nBienvenue au jeu du pendu ! Vous avez 3 niveaux de difficulté (facile, moyen, difficile): ".encode())
    niveau_choisi = mySocket.recv(1024).decode().lower()  
    
    while niveau_choisi not in niveaux:
        mySocket.send("Niveau invalide. Fermeture de la connexion.".encode())
        mySocket.close()
        return

  
    lettre_trouvée = "" #variable permetant de répertorier les lettres correctes trouvées
    lettre_utilisée = [] #variable permetant de répertorier les lettres utilisées 
    Mot = "" #variable permettant d'afficher au fur et à mesure le mot à deviner 
    b = True #les variables b, c, n et j sont des variables utilisées pour vérifier une condition 
    c = True 
    n = True
    j = ""
    solution = choisir_niveau(niveau_choisi) 
    
    tentative = 7
    
    for i in solution :
        Mot = Mot + "_ "
#boucle permettant d'afficher des "_" en fonction du nombre de lettre à trouver  

#Début du jeu avec la boucle while tant que b est vrai
    while b : 
        print(f"Le mot à trouver est : {solution}")
        print ("Mot à deviner :",Mot) #Afficher la variable Mot 
        mySocket.send(f"Mot à deviner : {Mot}\n".encode())

        if "_" not in Mot:
            mySocket.send(f">>> Bravo vous avez trouvé le mot à deviner << {solution} >> en {tentative} tentative ! <<<\n".encode())
            print(f">>> Bravo vous avez trouvé le mot à deviner en {tentative} tentative ! <<<")
            break #break permet de sortir directement du programme 
        #condition if permettant de vérifier si la variable Mot ne contient plus de "_". 
        # Si Mot n'a plus de "_", affichage victoire 
        
        #Boucle permettant de vérifier si l'utilisateur n'utilise pas plusieurs fois la même lettre 
        while n : #Tant que n vrai< 
            a = mySocket.recv(1024).decode() #affichage d'un champ permettant à l'utilisateur de choisir une lettre
            print(f"lettre choisi : {a}")

            if len(lettre_utilisée) == 0 : #conditions if permettant de vérifier si la variable lettre_utilisé est vide 
                n = False 
            #si elle est vide, on sort de la boucle "while n"

            if len(lettre_utilisée) != 0 : #conditions if permettant de vérifier si la variable lettre_utilisé n'est pas vide
                for w in range(len(lettre_utilisée)) : #boucle for permettant de parcourir toutes les lettres que contient la variable lettre_utilisée
                    if a == lettre_utilisée[w] : #conditions if permettant de vérifier si la lettre choisi a déjà été utilisé
                        j = True
                        n = True 
                        break
                    else : 
                        j = False 
                        n = False 
            

            if j == True : #condition if permettant d'avertir l'utilisateur qu'il a déjà utilisé cettre lettre 
                mySocket.send(f"La lettre {a} a déjà été utilisé.\n".encode())
                print("La lettre",a,"a déjà été utilisé.")

        d = len(a) #variable d contenant la longueur de la variable a 
        
        if d <= 1: #condition if permettant de vérifier si la variable a est une lettre 
            
            for l in solution : #boucle for permettant de parcourir les lettres dans solution
                if a == l : #condition if permettant de vérifier si la lettre choisi correspond à une lettre dans le mot à deviner 
                    c = True 
                    break
                else :
                    c = False 
                    
            if c == True : #condition if permettant d'afficher que la lettre est correcte si la lettre choisi se trouve dans la variable solution
                mySocket.send(f" La lettre {a} est correct !\n".encode())
                print("La lettre",a,"est correct !")
                lettre_trouvée = lettre_trouvée + " " + a #ajout de la lettre choisi dans la variable lettre_trouvée
                mySocket.send(f"Les lettres {lettre_trouvée} sont correct.\n".encode())
                print("Les lettres",lettre_trouvée,"sont correct.")
                lettre_utilisée.append(a) #ajout de la lettre choisi dans le tableau lettre_utilisé 
                mySocket.send(f"Il vous reste {tentative} tentative.\n".encode())
                print("Il vous reste",tentative,"tentative.")
                Mot = "" #variable permettant d'afficher au fur et à mesure le mot à deviner  
                for x in solution: #boucle for permettant de parcourir toutes les lettres dans solution
                    if x in lettre_trouvée : #conditions if permettant de vérifier si les lettres dans la variable lettre_trouvée correspondent aux lettres dans solution
                        Mot += x + " " #remplace les "_" par la lettre trouvée 
                    else:
                        Mot += "_ " #ne remplace rien

            else : #condition else permettant d'afficher que la lettre est incorrecte si la lettre choisi ne se trouve pas dans la variable solution
                mySocket.send(f"La lettre {a} est incorrect !\n".encode())
                print("La lettre",a,"est incorrect !")
                lettre_utilisée.append(a) #ajout de la lettre choisi dans le tableau lettre_utilisé
                tentative = tentative - 1 #on retire une tentative si la lettre est incorrecte 
                mySocket.send(f"Il vous reste {tentative} tentative.\n".encode())
                print("Il vous reste",tentative,"tentative.")
            
            if tentative==0: #condition if permettant d'afficher la défaite, le mot à deviner et le pendu si l'utilisateur n'a plus de tentative 
                mySocket.send(f"Vous n'avez plus de tentative, vous avez perdu.\n".encode())
                print("Vous n'avez plus de tentative, vous avez perdu.")
                mySocket.send(f"Le mot à deviner était, {solution} .\n".encode())
                print("Le mot à deviner était",solution,".")
                b = False 
                mySocket.send(f"==========Y=\n".encode())
                print(" ==========Y= ")
            if tentative<=1: #condition if permettant d'afficher la 6ème partie du pendu
                mySocket.send(f" ||/       |  \n".encode())
                print(" ||/       |  ")
            if tentative<=2: #condition if permettant d'afficher la 5ème partie du pendu
                mySocket.send(f" ||        0  \n".encode())
                print(" ||        0  ")
            if tentative<=3: #condition if permettant d'afficher la 4ème partie du pendu
                mySocket.send(f" ||       /|\ \n".encode())
                print(" ||       /|\ ")
            if tentative<=4: #condition if permettant d'afficher la 3ème partie du pendu
                mySocket.send(f" ||       / \  \n".encode())
                print(" ||       / \  ")
            if tentative<=5: #condition if permettant d'afficher la 2ème partie du pendu             
                mySocket.send(f"/||           \n".encode())
                print("/||           ")
            if tentative<=6: #condition if permettant d'afficher la 1ème partie du pendu
                mySocket.send(f"==============\n".encode())
                print("==============\n") 
        
        else : #condition else permettant de vérifier si la variable a est un mot
            if a == solution : #condition if permettant de vérifier si le mot choisi est le mot à deviner 
                print("Bravo vous avez trouvé le mot à deviner en",tentative, "tentative !")
                mySocket.send(f"Bravo vous avez trouvé le mot à deviner en {tentative} tentative !\n".encode())
                b = False
            else : #condition else permettant de vérifier si le mot choisi est incorrecte 
                tentative = tentative - 1
                print("Dommage ce n'est pas le bon mot. Il vous reste",tentative, "tentative.")
                mySocket.send(f"Dommage ce n'est pas le bon mot. Il vous reste {tentative} tentatives.\n".encode())
        n = True #variable n remit a True pour pouvoir effecture vérifier si l'utilisateur n'utilise pas une lettre déjà utilisée 

def main():
    global clients  # Utilise une variable globale pour suivre le nombre de clients connectés
    host = socket.gethostname()
    port = 12345

    server_socket = socket.socket()  # Crée un socket pour le serveur
    server_socket.bind((host, port))  # Attache l'adresse de l'hôte et le port au socket
    server_socket.listen(2)  # Limite à 2 clients simultanés

    # "f" indique à Python d'évaluer les expressions à l'intérieur des accolades {} et de les remplacer par leurs valeurs respectives.
    print(f"Le serveur écoute sur le port {port}...")

    while True:
        client_socket, addr = server_socket.accept()  # Accepte une nouvelle connexion cliente

        if clients < 2:  # Vérifie s'il y a de la place pour un nouveau client
            clients += 1  # Incrémente le nombre de clients connectés
            
            #threads: permet au programme d'accomplir plusieurs tâches en même temps,
            #on crée un nouvel objet de type thread avec la classe Thread du module threading.
            #target spécifie la fonction que le thread exécutera. 
            #args spécifie les arguments à passer à la fonction (jeu_pendu)
            client_pendu = threading.Thread(target=jeu_pendu, args=(client_socket,))
            #On crée un nouveau thread (client_pendu) qui exécutera la fonction jeu_pendu 
            #avec le socket spécifique du client en tant qu'argument.
            
            client_pendu.start()  # On démarre le thread, la fonction jeu_pendu 
            #commence à s'exécuter de manière indépendante dans ce thread. 
            #cela permet au serveur de continuer à accepter d'autres connexions pendant 
            #que chaque client est géré.
        else:
            print("Nombre maximal de clients atteint. Refus de la connexion.")
            client_socket.close()  # Ferme la connexion du client si le nombre maximal est atteint

if __name__ == "__main__":
    main()
