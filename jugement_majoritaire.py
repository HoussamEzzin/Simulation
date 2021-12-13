import random
nbElecteur = 8
nbCandidats = 3
nbMention = 7

votes = dict()

for e in range(1,nbElecteur):
    for c in range(1,nbCandidats):
        votes[e] = random.randint(1,nbMention)

for c in nbCandidats:
    for m in nbMention:
        resultat = 0
        for e in nbCandidats:
            pass
#still uncomplete