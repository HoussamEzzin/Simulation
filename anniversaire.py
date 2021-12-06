import random

nb_persons = 25 

nb_simulation = 10000

days = []
mounths = []

chance = 0
score = 0
person = []
progress = 0
for i in range(nb_simulation):
    progress += 1
    print((progress/nb_simulation)*100)
    days = [random.randint(1,365) for x in range(25)]
   
    for j in range(len(days)):
        if days.count(days[j]) == 2:
            score += 1
            break
    
print(days)
chance = (score/nb_simulation)*100
print('chance : ', chance)
    
    
        