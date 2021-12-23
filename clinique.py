import simpy

nb_heures = 20

# events : 
# 1 - arrivee d'un patient
# 2 - servi par infermier 18mm
# 3 - servi par medecin 25mm

def arrive(env,serveur,temps_arrivee):
    i = 0
    while True:
        print('Client %d arrive a %d' % (i, env.now))
        env.process(traitement(env,i,serveur))
        yield env.timeout(temps_arrivee)
        i +=1

def traitement(env,i,serveur):
    print('Client %d demande infermier a %d' % (i,env.now))
    with serveur.request() as req:
        yield req
        print('Client %d se traite par infermier a %d'%(i,env.now))
        yield env.timeout(7)
        print('Client %d termine avec infermier a %d'%(i,env.now))
    print('Client %d demande medecin a %d' % (i,env.now))
    with serveur.request() as req:
        yield req
        print('Client %d se traite par medecin a %d'%(i,env.now))
        yield env.timeout(25)
        print('Client %d termine avec medecin a %d'%(i,env.now))

    
    
env = simpy.Environment()
nb_med = 20
medecin = simpy.Resource(env, capacity=nb_med)
nb_inf = 40
infermier = simpy.Resource(env, capacity=2)

env.process(arrive(env,infermier,7))
env.process(arrive(env,medecin,7))
env.run(until=70)

