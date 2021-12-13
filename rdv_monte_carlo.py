
import random
somme = 0
nb_simulation = 1000


for i in range(nb_simulation):
    arrive1 = random.randint(0,60)
    arrive2 = random.randint(0,60)
    attente = abs(arrive1 - arrive2)
    somme += attente

moyenne = somme/nb_simulation
print("Estimation de la moynner est :", moyenne)
        


# todo : 3 persons or more .. (n)
# array of the minutes when they arrived
# max and min 
