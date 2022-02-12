import random

H = 0 # horloge de simulation
i = 1 # numero client arrive a chaque fois.
LQ = 0 #Longueur queue
NCP = 0 # nombre clients perdus
NCE = 0 #nombre clients entres
C1 = 0 #etat caisse 1 libre
C2 = 0 # etat caisse 2 libre
calendrier = []
file = []

def inserer_file(ref):
    global file
    file.append(ref)
def supprimer_file(ref):
    global file
    file.remove(ref)

def planifier_evt(ref,type,date):
    evt = {
        "ref":ref,
        "type":type,
        "date":date
    }
    calendrier.append(evt)
    
def F1(alea):
    if(alea >= 0 and alea < 0.3):
        return 1
    elif(alea >= 0.3 and alea <= 0.8):
        return 2
    elif(alea > 0.8 and alea <= 0.9):
        return 3
    elif(alea > 0.9 and alea <= 0.95):
        return 4
    elif(alea > 0.95 and alea <= 0.98):
        return 5
    elif(alea > 0.98 and alea <= 1):
        return 6

def F2(alea):
    if(alea >= 0 and alea < 0.1):
        return 2
    elif(alea >= 0.1 and alea <= 0.3):
        return 4
    elif(alea > 0.3 and alea <= 0.7):
        return 6
    elif(alea > 0.7 and alea <= 0.9):
        return 8
    elif(alea > 0.9 and alea <= 1):
        return 10

def F3(alea):
    if(alea >= 0 and alea < 0.2):
        return 1
    elif(alea >= 0.2 and alea <= 0.6):
        return 2
    elif(alea > 0.6 and alea <= 0.85):
        return 3
    elif(alea > 0.85 and alea <= 1):
        return 4

def selectionner_evt(ref,type,date):
    print(ref,type,date)
    print("Selectionne")
    
def arrivee(ref):
    global LQ,NCE,NCP,i
    if(LQ <= 1):
        NCE = NCE +1 
        planifier_evt(ref,"FM",H+F2(random.random()))
    else:
        NCP = NCP + 1
    i = i + 1
    DA = H + F1(random.random())
    if DA <= 720 :
        planifier_evt(i,"A",DA)

def fin_magasinage(ref):
    global C1, C2, LQ
    if C1 == 0 or C2 == 0:
        if(C1 == 0):
            C1 = ref
        else:
            C2 = ref
        planifier_evt(ref,"FP",H+F3(random.random()))
    else :
        LQ = LQ + 1
        inserer_file(ref)
        
def fin_paiement(ref):
    global C1,C2,file,LQ
    if LQ == 0:
        if C1 == ref:
            C1 = 0
        else: 
            C2 = 0
    else:
        J = file[0]
        supprimer_file(J)
        LQ = LQ -1 
        if C1 == ref:
            C1 = J
        else:
            C2 = J
        planifier_evt(J,"FP",H +F3(random.random()))
    
        
                

planifier_evt(1,"A",F1(random.random()))
while(len(calendrier)!=0):
    evt = calendrier[0]
    selectionner_evt(evt.ref,evt.calendrier[0].type,evt.calendrier[0].date)
    H = evt.date
    if(evt.type == "A"):
        arrivee(evt.ref)
    elif(evt.type == "FM"):
        fin_magasinage(evt.ref)
    elif(evt.type == "FP"):
        fin_paiement(evt.ref)
DFS = H
print(NCP,NCE,DFS)

