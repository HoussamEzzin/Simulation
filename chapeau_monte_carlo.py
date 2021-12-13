import random

nb_sim = 5000




def get_random_hat(n):
    l = list(range(n))
    s= []
    while len(l) > 0:
        tirage = random.choice(l)
        l.remove(tirage)
        s.append(tirage)
    return s

def simul(nb):
    n = 50
    score = 0
    progress = 0
    for s in range(nb):
        print("Progress :",(progress/nb)*100,"%")
        progress +=1
        hats = get_random_hat(nb)
        for p in range(n):
            if hats[p] == p:
                score +=1
                break
    return score/nb

def main():
    print("Proba :" ,simul(nb_sim)*100,"%")
    

if __name__ == "__main__":
    main()


    