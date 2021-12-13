import random
nb_simulation = 5000


somme = 0
for i in range(nb_simulation):
    des_array =[random.randint(1,7) for x in range(5)]
    count = 5
    for des in des_array:
        if des == 1:
            count -= 1
    
    somme += count

moyenne = somme/nb_simulation

print("Moynne  :", moyenne)