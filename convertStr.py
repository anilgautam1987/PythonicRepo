from pprint import pprint
import sys
import collections


def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

print(toStr(1453,16))

# 4 * 3 * 2 * 1 = 24 
def factorial(num):
    if num < 2:
        return 1    
    return num * factorial(num - 1)

#0 1 1 2 3 5 

def fibonacci(num):    
    a,b = 0,1 
    for i in xrange(0,num):       
        yield "{:0}:{:0}".format(i+1, a)
        a,b = b , a + b 
        
for item in fibonacci(10):
    print item
    

def listsum(numList):
    
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])
    
print listsum([3,5,6,7,8])

def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr

print(match_words(['abc', 'xyz', 'aba', '1221']))


def last(n): 
    return n[-1]

def sorted_list(tuples):
    return sorted(tuples, key=last)

print(sorted_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


def removeduplicate(aList):
    
    dup_item = set()    
    uniq_item = []
    
    for x in aList:
        if not x in dup_item:
            uniq_item.append(x)
            dup_item.add(x)
    print(dup_item)

a = [10,20,30,20,10,50,60,40,80,50,40] 
print 'removeduplicate =:',removeduplicate(a)

#find the list of words that are longer than n from a given list of words.
def log_words(n, s):
    
    words = []
    xwords = s.split(" ")
    for x in xwords:
        if len(x) > n:
            words.append(x)
    return words
print(log_words(3,"This is my Python programm to test strings"))
 
def common_members(aList, bList):
    common_list = []
    
    for x in aList:
        if x in bList:
            common_list.append(x)
    return common_list 

print 'Common_List' , common_members( [1,2,4], [2,5,6,6])

#program to print a specified list after removing the 0th, 4th and 5th elements.
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print 'colors before reduction =:' , color
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print 'colors after reduction =:' , color 

#Python program to generate a 3*4*6 3D array whose each element is *

array = [  [ [ '*'  for col in range(6) ]  for col in range(4) ] for row in range(3) ]
pprint(array)

#program to print the numbers of a specified list after removing even numbers from it
L = [120,45,6,7,8,77,12,33,14]
aList = [x for x in L if x%2 != 0]
print 'List =:' , aList

#program to shuffle and print a specified list
from random import shuffle 
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(color)
print(color)

def printValues():
    L = list()
    for i in range(1,21):
        L.append(i**2)
    print(L)
    print 'First Five =:' , L[:5]
    print 'Last  Five =:' , L[-5:]
    
printValues()

#Generate all permutations of a list in Python 
import itertools
print(list(itertools.permutations([1,2,3])))

for index , value in enumerate([11,22,33,44,55]): 
    print 'Index  : {0} Value : {1}'.format(index , value)
     
'''
program to check whether two lists are circularly identical    
''' 

def isCircular(alist,bList):
    
    if len(alist) != len(bList):
        return False
    
    str1  = ' '.join(map(str, alist))
    str2  = ' '.join(map(str, bList))    
     
    if len(str1) != len(str2):
        return False
    
    return str1 in str2 + ' ' + str2 

list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [10, 10, 10, 0, 0]
list4 = [1, 10, 10, 0, 0]

print isCircular(list1, list2)
print isCircular(list1, list3)


'''
 Find the second smallest number in a list
'''

def second_smallest(aList):
    #inf - infinity and Nan means Not a Number
    a1, a2 = float('inf') , float('inf')
    
    for x in aList:           
        if x <= a1:
            a1, a2 = x , a1
        elif x < a2:
            a2 =x 
    return a2
print second_smallest([11,3,4,53,32])


def second_largest(aList):
    count = 0 
    n1 = n2 = float('-inf')
    for x in aList:
        count += 1 
        if x > n2:
            if x >= n1:
                n1 , n2 = x , n1 
            else:
                n2 = x 
    return n2 if count >= 2 else None
print( second_largest([11,3,4,53,32]))


def second_largest_method2(aList):
    m1 = m2 = None 
    if aList[0] > aList[1]:
        m1 , m2 = aList[0] , aList[1]
    elif aList[0] < aList[1]:
        m2 , m1 = aList[1] , aList[0] 
    
    for x in aList:
        if x < m2:
            if x < m1:
                m2 , m1 = x , m2 
            else: 
                m2 = x
    return m2
#print( second_largest([20,67,3,2.6,7,74,2.8,90.8,52.8,4,3,2,5,7]))
    
def multiplyList(aList):
    
    total = 1
    for item in aList:
        total = total * item
    return total
print multiplyList([2,3,4])  

#Python program to flatten a shallow list.

orginal_lst = [[23,45,55] , [24,67] , [9,20] , [10]]
new_list    = list(itertools.chain(*orginal_lst))
print new_list

#Python program to select an item randomly from a list. 
import random
color_list = ["red", "green" , "blue" , "white"]
print(random.choice(color_list))

#Write a Python program to get the frequency of the elements in a list.
my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
cntr   = collections.Counter(my_list)
print cntr

#Write a Python program to generate all sublists of a list.
''' 
Ex: l1 = [10, 20, 30, 40]
[[], [10], [10, 20], [10, 20, 30], [10, 20, 30, 40], [20], [20, 30], [20, 30, 40], [30], [30, 40], [40]]      
''' 
def generate_subslists(myList):
    subs = [[]] 
    for i in range(len(myList)):
        n = i + 1
        while(n<=len(myList)):
            sub = myList[i:n]
            subs.append(sub)
            n = n + 1
    return subs 

li = [10,20,30,40]
print generate_subslists(li)


#Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
#Sample list : ['p', 'q']
#n =5
#Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

my_list = ['p', 'q']
n = 4
new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]
print(new_list)


def generate_dict(n):
    d = {i:i*i for i in range(1, n)}
    return d
d = generate_dict(5)
mySum = sum(d.values())
print 'MySum=:' , mySum


def multiply_dict(d):
    result=1
    for k in d:
        result = result * d[k]
    return result
print multiply_dict(d)

a = set(["Jake", "John", "Eric"])
print "Sets A  =:"
print(a)
print "Sets B  =:"
b = set(["John", "Jill"])
print(b)

e = a.difference(b)
print "Sets e=:" , e
f = a.intersection(b)
print "Sets f=:" , f
g = b.difference(a)
print "Sets G=:" , g


my_dict = {'x':500, 'y':5874, 'z': 560}
key_max = max(my_dict.keys() , key=(lambda k:my_dict[k]))
key_min = min(my_dict.keys() , key=(lambda k:my_dict[k]))


print 'Key Min =:' , key_min
print 'Key Max =:' , key_max

# Unique values in Dictionary 
L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
values = set( [val for d in L for val in d.values()] ) 
print 'Values =:' , values

''' program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
 Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output: 
ac
ad
bc
bd
''' 
d ={'1':['a','b'], '2':['c','d']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))

''' Write a Python program to find the highest 3 values in a dictionary. ''' 

from heapq import nlargest
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}  
three_largest = nlargest(3, my_dict , key=my_dict.get)
print 'three_largest =:' , three_largest

item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
from collections import Counter
result = Counter()
for d in item_list:    
    result[d['item']] +=d['amount']

print(result)

class Node(object):
    def __init__(self,data):
        self.data = data 
        self.next = None


class LinkedList(object):
    
    def __init__(self):
        self.head = None 
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head     = new_node
    
    def swap_element(self):
        temp = self.head 
        
        if temp is None:
            return 
        
        while (temp is not None and temp.next is not None):
            #cuurent data swap with NEXT->data
            temp.data , temp.next.data = temp.next.data , temp.data
            temp = temp.next.next 
    
    def printList(self):
        temp = self.head
        while temp:
            print temp.data
            temp = temp.next

linklst = LinkedList()
linklst.push(10)
linklst.push(9)
linklst.push(11)
linklst.push(12)
linklst.push(21)
linklst.push(31)

print '********** Before Swap ******'
print linklst.printList() 
linklst.swap_element()
print linklst.printList()

''' Write a Python program to create a dictionary from a string. ''' 
str1 = 'anilGautam'
my_dict = {}
for letter in str1:    
    my_dict[letter] = my_dict.get(letter , 0) + 1
print(my_dict) 


from collections import Counter
letter_counter = Counter()
for letter in 'the quick brown fox jumps':
    letter_counter[letter] += 1 
print letter_counter






    