solution = "chat"
tentative = 10
lettre_trouvée = ""
lettre_incorrect = ""
Mot = ""
b = True
c = True 

for i in solution :
    Mot = Mot + "_ "

while b : 
    print ("Mot à deviner :",Mot)
    
    if "_" not in Mot:
        print(">>> Bravo vous avez trouvé le mot à deviner en",tentative, "tentative ! <<<")
        break
    
    a = str(input("Choisir une lettre ou un mot : "))
    print ("Vous avez choisi :", a)
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
            print("Il vous reste",tentative,"tentative.")
            Mot = ""
            for x in solution:
                if x in lettre_trouvée :
                    Mot += x + " "
                else:
                    Mot += "_ "

        else :
            print("La lettre",a,"est incorrect !")
            lettre_incorrect = lettre_incorrect + " " + a
            tentative = tentative - 1
            print("Les lettres",lettre_incorrect,"sont incorrect.")
            print("Il vous reste",tentative,"tentative.")

        if tentative == 0 :
            print("Vous n'avez plus de tentative, vous avez perdu.")
            b = False 
    
    else : 
        if a == solution :
            print(">>> Bravo vous avez trouvé le mot à deviner en",tentative, "tentative ! <<<")
            b = False
        else :
            tentative = tentative - 1
            print("Dommage ce n'est pas le bon mot. Il vous reste",tentative, "tentative.")