list = ['a', 'b', 'c', 'd', 'e']
print list[10:]


class C:
  dangerous = 2
  
c1 = C()
c2 = C()

print c1.dangerous #2

c1.dangerous = 3
print c1.dangerous #3
print c2.dangerous #2

del c1.dangerous 
print c1.dangerous #2
 
C.dangerous = 3
print c2.dangerous #3

print range(0, 10 , 1)
print range(10, -11, -1)

n = [0,1,2,3,4,5]

print n[::2]


spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'hello'
print spam

