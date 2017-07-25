from _ast import Num
L = [1,2,3]

def permutaiton(L):    
    length = len(L)
    if length <=1:
        yield L
    else:
        for n in range(0, length):
            for end in permutaiton(L[:n] + L[n+1:]):
                yield [L[n]] + end

for x in permutaiton(L):
    print x

def reverseInterger(num):    
    reverse = 0 
    while num >0:
        reminder = num % 10
        reverse  = (reverse * 10) + reminder 
        num //= 10
    return reverse
num = 131
reverse = reverseInterger(num)
print 'Reverse Number %d' % reverse 

if reverse == int(num):
    print 'Number {0} is a palindrome'.format(num)
    
def evenFibo(n):
    a , b = 1 , 1
    total = 0  
    while a< n:
        if a % 2 == 0:
            total += a 
        a , b = b , a + b 
    return total
print evenFibo(50)


#Find the sum of all the multiples of 3 or 5 below 1000.
print sum([i for i in range(1000) if i % 3 ==0 or i % 5 == 0])

#Largest prime factor

def primeFactors(num):
    factors = []
    i = 2
    while i * i <=n:
        if n % i:
            i += 1
        else:
            n //= i 
            factors.append(i)
        
    if n > 1:
        factors.append(n)
    return factors



