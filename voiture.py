import simpy

def car(env):
    while True:
        print("Start parking at {:d}".format(env.now))
        parking_duration = 5
        yield env.timeout(parking_duration)
        print("Start driving at {:d}".format(env.now))
        trip_duration = 12
        yield env.timeout(trip_duration)
        
        
    
env = simpy.Environment()
env.process(car(env))
env.run(until=20)