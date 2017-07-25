import timeit

t1 = timeit.default_timer()
a = 0
for i in xrange(1, 100000000):
    pass
t2 = timeit.default_timer()

print "time taken: ", (t2-t1)  # 4.49153590202 seconds

t1 = timeit.default_timer()
a = 0
for i in range(1, 100000000):
    pass
t2 = timeit.default_timer()

print "time taken: ", (t2-t1)  # 17