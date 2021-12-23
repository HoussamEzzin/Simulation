import simpy

def arrive(env, serveur, tempsArrive):
    i = 0
    while True:
        print("Client %d arrive a %d" % (i, env.now))
        env.process(finService(env,i,serveur,20))
        yield env.timeout(tempsArrive)
        i +=1

def finService(env, i, serveur, tempsService):
    print('Client %d demande le service a %d'%(i, env.now) )
    with serveur.request() as sr: 