print 'This topic covers all list comprehension in python \n'

# Basic syntax for List Comprehension 
#    [<expression> for <item> in <sequence> if  <condition>]

Lst = range(2,201)

# List Comprehension
my_prime = [x for x in Lst if all( (x % y != 0  for y in range(2,x)))]
print my_prime

# Dictionary Comprehension 
letters = ['a','b','c','d']
words   = ['apple','banana' , 'cat' , 'dog']

my_dict_method1 = { k:v  for k , v  in zip(letters , words )}
print my_dict_method1

my_dict_method2 = dict([ (k,v) for k , v in zip(letters, words) ] )
print my_dict_method2 

# Sets Comprehension
my_dict = { (k,v)  for k , v  in zip(letters , words )}
print my_dict

# Touple Comprehension
lst = [2,4,6,8]
my_iterator = (n*n for n in lst)
print next(my_iterator)
