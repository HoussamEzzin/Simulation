import random

nb_persons = 25 

nb_simulation = 10000


score = 0
progress = 0
for i in range(nb_simulation):
    progress += 1
    print((progress/nb_simulation)*100)
    persons = [random.randint(1,365) for x in range(25)]
    
    for j in range(len(persons)):
        if persons.count(persons[j]) == 2:
            score += 1
            break
    
print("Size :",len(persons))
chance = (score/nb_simulation)*100
print('chance : ', chance)
    
    
        