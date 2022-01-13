import simpy
def client(e, r, s,arrival_time):
    yield e.timeout(2)
    print('%s Tâche1 à : %d' % (r, e.now))
    with s.request() as req:
        yield req
        print('%s Tâche2 à : %d' % (r, e.now))
        yield e.timeout(arrival_time)
        print('%s Tâche3 à : %d' % (r, e.now))
e = simpy.Environment()
s = simpy.Resource(e, capacity=3)
for i in range(1, 6):
    e.process(client(e, 'Client : %d' % i, s,7))
e.run()