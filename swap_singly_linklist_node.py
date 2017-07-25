# Python program to swap the elements of linked list pairwise 

class Node(object):
    
    def __init__(self , data):
        self.data = data 
        self.next = None

        
class LinkedList(object):
    
    def __init__(self):
        self.head = None
        
    def pairwiseSwap(self):
        
        temp = self.head        
        # if there is no node in linked list
        if temp is None:
            return 
      
        # Traverse further only if there are at least two 
        # Left 
        while(temp is not None and temp.next is not None):
            temp.data , temp.next.data = temp.next.data , temp.data
            # move temp by 2 fro the next pair
            temp = temp.next.next
            
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def printList(self):
        temp = self.head
        while(temp):
            print temp.data 
            temp = temp.next
    
if __name__ == '__main__':
    llist = LinkedList()
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    
    # print element before swaping
    llist.printList()
        
    # swap pairwise list
    llist.pairwiseSwap()
    
    print "\n****** After pairswap list *********\n"
    # print after swap
    llist.printList()
    
    
    
        
            
    
            