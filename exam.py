import simpy
count = 0
def program_is_here(env, serveur,unites, arrival_time):
    i = 0
    while True:
        print('Program %d is here at %d' % (i, env.now))
        env.process(program_finished(env, i ,serveur,unites))
        yield env.timeout(arrival_time)
        i +=1
def program_finished(env,i , serveur,unites):
    global count
    print('Program %d asks for server at %d '% (i,env.now))
    with serveur.request() as req:
        yield req
        print('Program %d is being serverd by a server at %d' %(i,env.now))
        yield env.timeout(0.018)
        print('Program %d finish with server at %d'%(i, env.now))
    print('Program %d asks for doctor at %d '% (i,env.now))
    with unites.request() as req:
        yield req
        print('Program %d is being treated by unites at %d' %(i,env.now))
        yield env.timeout(0.024)
        print('Program %d finish with unites at %d'%(i, env.now))
    count +=1
    print("*****Program %d is completed"%(i))
env = simpy.Environment()
serveur = simpy.Resource(env, capacity=20)
unites = simpy.Resource(env, capacity=30)
env.process(program_is_here(env,serveur,unites,0.07))
env.run(until=60)