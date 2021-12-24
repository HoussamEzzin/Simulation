import simpy
count = 1
def patient_is_here(env, nurse,doctor, arrival_time):
    i = 0
    while True:
        print('Patient %d is here at %d' % (i, env.now))
        env.process(patient_treated(env, i ,nurse,doctor))
        yield env.timeout(arrival_time)
        i +=1
def patient_treated(env,i , nurse,doctor):
    global count
    print('Patient %d asks for nurse at %d '% (i,env.now))
    with nurse.request() as req:
        yield req
        print('Patient %d is being treated by a nurse at %d' %(i,env.now))
        yield env.timeout(18)
        print('Patient %d finish with nurse at %d'%(i, env.now))
    print('Patient %d asks for doctor at %d '% (i,env.now))
    with doctor.request() as req:
        yield req
        print('Patient %d is being treated by a doctor at %d' %(i,env.now))
        yield env.timeout(25)
        print('Patient %d finish with doctor at %d'%(i, env.now))
    count +=1
    print("*****Patient %d is fully treated"%(i))
env = simpy.Environment()
nurse = simpy.Resource(env, capacity=4000)
doctor = simpy.Resource(env, capacity=4000)
env.process(patient_is_here(env,nurse,doctor,7))
env.run(until=60*8)


# for i in range(1,5):
#     for j in range(1,6):
#         print(str(i)+"//"+str(j))
for i in range(1,6):
    for j in range(1,5):
        
        print(str(i)+"//"+str(j))