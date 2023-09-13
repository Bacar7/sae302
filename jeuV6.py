import random

choix = ["rhinopharyngitolaryngographologiquement", "cyclopentanoperhydrophénanthrène", "voiture", "camion", "moto", "avion", "chat", "chien", "souris", "éléphant", "ordinateur", "téléphone", "tablette", "écouteur"]

tentative = 7
lettre_trouvée = ""
lettre_utilisé = []
Mot = ""
b = True
c = True 
n = True
j = ""
solution = random.choice(choix)


for i in solution :
    Mot = Mot + "_ "

while b : 
    print ("Mot à deviner :",Mot)

    if "_" not in Mot:
        print(">>> Bravo vous avez trouvé le mot à deviner en",tentative, "tentative ! <<<")
        break
    
    while n :
        a = str(input("Choisir une lettre ou un mot : "))
        print ("Vous avez choisi :", a)

        if len(lettre_utilisé) == 0 : 
            n = False 

        if len(lettre_utilisé) != 0 :
            for w in range(len(lettre_utilisé)) :
                if a == lettre_utilisé[w] :
                    j = True
                    n = True 
                    break
                else : 
                    j = False 
                    n = False 

        if j == True : 
            print("La lettre",a,"a déjà été utilisé.")

    d = len(a)
     
    if d <= 1: 
        
        for l in solution : 
            if a == l :
                c = True 
                break
            else :
                c = False 
                
        if c == True :
            print("La lettre",a,"est correct !")
            lettre_trouvée = lettre_trouvée + " " + a
            print("Les lettres",lettre_trouvée,"sont correct.")
            lettre_utilisé.append(a)
            print("Il vous reste",tentative,"tentative.")
            Mot = ""
            for x in solution:
                if x in lettre_trouvée :
                    Mot += x + " "
                else:
                    Mot += "_ "

        else :
            print("La lettre",a,"est incorrect !")
            lettre_utilisé.append(a)
            tentative = tentative - 1
            print("Il vous reste",tentative,"tentative.")
        
        if tentative==0:
            print("Vous n'avez plus de tentative, vous avez perdu.")
            b = False 
            print(" ==========Y= ")
        if tentative<=1:
            print(" ||/       |  ")
        if tentative<=2:
            print(" ||        0  ")
        if tentative<=3:
            print(" ||       /|\ ")
        if tentative<=4:
            print(" ||       / \  ")
        if tentative<=5:                    
            print("/||           ")
        if tentative<=6:
            print("==============\n") 
    
    else : 
        if a == solution :
            print("Bravo vous avez trouvé le mot à deviner en",tentative, "tentative !")
            b = False
        else :
            tentative = tentative - 1
            print("Dommage ce n'est pas le bon mot. Il vous reste",tentative, "tentative.")
    n = True 