print 'This is to demonstrate the map with lambda function'
def sqr(n):
    return n * n 

lst = [2,3,4,6]
print map(lambda x: sqr(x) , lst) 


def triple(value):
    return value * value 

def triplestuff(a_lst):
    return map(lambda x: triple(x) , a_lst)

def qudrastuff(a_lst):
    return map(lambda x: 4*x , a_lst)

lst = [2,3,4,6] 
print triplestuff(lst)
print qudrastuff(lst)

