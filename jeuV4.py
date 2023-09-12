solution = "chat"
tentative = 10
lettre_utilisé = []
Mot = ""
b = True
c = True 
n = True
j = ""
h = 1

for i in solution :
    Mot = Mot + "_ "

while b : 
    print ("Mot à deviner :",Mot)
    
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
            lettre_utilisé.append(a)
            print("Il vous reste",tentative,"tentative.")

        else :
            print("La lettre",a,"est incorrect !")
            lettre_utilisé.append(a)
            tentative = tentative - 1
            print("Il vous reste",tentative,"tentative.")
        
        if tentative == 0 :
            print("Vous n'avez plus de tentative, vous avez perdu.")
            b = False 
    
    else : 
        if a == solution :
            print("Bravo vous avez trouvé le mot à deviner en",tentative, "tentative !")
            b = False
        else :
            tentative = tentative - 1
            print("Dommage ce n'est pas le bon mot. Il vous reste",tentative, "tentative.")
    n = True 
    h = 1