# Librairie 
import socket    

# Variable
solution = "chat"
tentative = 10
lettre_trouvée = ""
lettre_incorrect = ""
Mot = ""
b = True
c = True 
n = True
j = "" 
data = ""
host = socket.gethostname()                
port = 5000                
maSocket = socket.socket()                  
maSocket.bind((host, port))                 

maSocket.listen(1)                  
conn, address = maSocket.accept()                   
print("Connexion de : " + str(address))

for i in solution :
    Mot = Mot + "_ "

while b : 
    data = Mot    
    conn.send(data.encode())

    while n :
        data = conn.recv(1024).decode()
        print("Le client a choisi la lettre ou le mot : " + str(data))
        
        if data == j :
            conn.send(data)
        else : 
            n = False

    d = len(data)
     
    if d <= 1: 
        
        for l in solution : 
            if data == l :
                c = True 
                break
            else :
                c = False 
                
        if c == True :
            lettre_trouvée = lettre_trouvée + " " + data
            e = "La lettre",data,"est correct ! Les lettres",lettre_trouvée,"sont correct. Il vous reste",tentative,"tentative."
            conn.send(e)

        else :
            lettre_incorrect = lettre_incorrect + " " + data
            tentative = tentative - 1
            f = "La lettre",data,"est incorrect ! Les lettres",lettre_incorrect,"sont incorrect. Vous n'avez plus de tentative, vous avez perdu."
            conn.send(f)
            
        if tentative == 0 :
            data = "Vous n'avez plus de tentative, vous avez perdu."
            conn.send(data)
            b = False 
    
    else : 
        if data == solution :
            data = "Bravo vous avez trouvé le mot à deviner en",tentative, "tentative !"
            b = False
        else :
            tentative = tentative - 1
            data = "Dommage ce n'est pas le bon mot. Il vous reste",tentative, "tentative."
    j = data
    n = True                   

conn.close()                    
