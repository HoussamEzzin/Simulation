import random
nb_simulation = 5000


somme = 0
smoke = True
for i in range(nb_simulation):
    boite1 =["*" for x in range(40)]
    boite2 =["*" for x in range(40)]
    smoke = True
    while smoke:
        choice = random.randint(1,2)
        if choice == 1:
            boite1.remove("*")
        else:
            boite2.remove("*")
        if len(boite1) == 0:
            somme += len(boite2)
            smoke = False
        if len(boite2) == 0:
            somme += len(boite1)
            smoke = False


moyenne = somme/nb_simulation
print("Moyenne :", moyenne)
        
    
    
    
    
    