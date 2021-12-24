import simpy

def arrive(env, server, arrival_time):
    i = 0
    while True:
        print('Client %d is here at %d' % (i, env.now))
        env.process(service_done(env,i, server,20))
        yield env.timeout(arrival_time)
        i += 1

def service_done(env, i , server, service_time):
    print('Client %d asks for service at %d' % (i,env.now))
    with server.request() as req:
        yield req
        #serve the client
        print('Client %d is being served at %d' % (i,env.now))
        yield env.timeout(service_time)
        print('Client %d finish service at %d' %(i,env.now))
        
env = simpy.Environment()
server = simpy.Resource(env, capacity = 3)
env.process(arrive(env,server,15))
env.run(until=70)