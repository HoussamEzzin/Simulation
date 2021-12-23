import simpy

def clock(env,name,tick):
    while True:
        print(name,env.now)
        yield env.timeout(tick)

env = simpy.Environment()
env.process(clock(env,'fast',1))
env.process(clock(env,'slow',2))
env.run(until=6)