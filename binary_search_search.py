'''
Created on Jun 24, 2017

@author: angautam
'''
class Node():
    
    def __init__(self,val,key,left,right):
        
        self.key = key 
        self.value = val 
        self.left  = left
        self.right = right 

def  dump(obj):    
    for attr in dir(obj):
        print "Obj %s == %s " % (attr , getattr(obj, attr))
    
import sys 
def search(value , p):
    #dump(p)  
    if(p.value == value):
        print( "You have bought {0}".format(p.key) )
        return
    else:
        if p.value < value:
            search(value, p.right)
        if p.value > value:
            search(value, p.left)
    

root = Node(3, "Chips" , None , None)
root.left = Node(4,"rasberrypi" , None ,None)
root.left.right = Node(6,"Mac" , None, None)
root.right = Node(5,"TV" , None , None)
root.right.left = Node(7, "Fridge" , None , None)

search(3, root)
