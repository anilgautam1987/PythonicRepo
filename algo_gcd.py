#Find the greatest common factor of (m,n) 
'''
        Step 1 : List of factors of m 
                [1,2,3,,4,5,6,7,8,9,10,11,13,14 ] - 14 / 14 
        Step 2 : List of factors of n
        Step 3 : Find the Largest number that comes on both list 
'''

def factors(num):
    
    list_factors = []
    for element in range(1, num+1):
        if num % element == 0:
            list_factors.append(element)
    return list_factors

def gcd(m,n):
    
    fm = factors(m)
    fn = factors(n)
    
    cf = []
    for f in fm:
        if f in fn:
           cf.append(f)    
    return cf[-1] 
    
def optimize_gcd(m,n):
    cf = []
    ''' Note (14,63):  min - 14 because greater then 14 is certainly cannot be a Factor of m or n , meeans 15 or 16 or so cannot divide 14 '''
    for i in range(1, min(m,n)+1):
        if ( m % i == 0 and n % i == 0):
            cf.append(i)
    return cf[-1]

def most_common_recent_factor_gcd(m,n):
    ''' Here we will be removing the list for finding the larget common factor by traversing backward to the min(m,n) '''
    ''' Search from end to the beginning ''' 
    i = min(m,n)    
    while i > 0:
        if (m % i == 0) and (n % i == 0):
            return i  
        else:
            i = i - 1

def gcd_with_recursion(m,n):
    
    if m < n:
        (m,n) = (n,m)
    
    if (m % n == 0):
        return n
    else:
        diff = m-n
        # diff > n ? Possible !! 
        return gcd_with_recursion( max(n , diff)  , min(n, diff))
    
print 'Common Factor =:' , gcd(14,63)
print 'Shortest way of GDC =:' , optimize_gcd(14,63)
print 'Most Common recent Factor =:' , most_common_recent_factor_gcd(14,63)
print 'Euclids GCD Factor =:' , gcd_with_recursion(14,63)


music = ["Abba","Rolling Stones","Black Sabbath","Metallica"]
print ' '.join(music)

a = [1,2,3]
print "".join(map(str , a))

