class Node():
    
    def __init__(self, data):
        self.data =  data
        self.left =  None
        self.right = None
        
''' Now we need to have a BST ''' 
class BST():
    def __init__(self):
        self.root = None
    
    # Lets create a method for adding Nodes, here a BST left node is always lesser then root and right node is always greater then root 
    def add_node(self,data):        
        #prepare a node
        node = Node(data)
        #For the fist node in the tree
        if self.root == None:
            self.root = node 
            return
        
        # Lets hande other in subtapi
        self._add_node(node, self.root)
    
    def _add_node(self, node , root):
        #if root is None
        if self.root == None:
            root = Node()
        elif not root.left and node.data < root.data:
            self.left = node 
        elif not root.right and node.data > root.data:
            self.right = node 
        elif root.data > node.data:
            self._add_node(node, root.left)
        elif root.data < node.date:
            self._add_node(node, root.right)
    
    def print_inorder_traversal(self):
        self._print_inorder_traversal(self.root)
    
    def _print_inorder_traversal(self, root):
        
        if not root:
            return
        self._print_inorder_traversal(root.left)
        print(root.data) 
        self._print_inorder_traversal(root.right)
            
bst = BST()
bst.add_node(5)
bst.add_node(2)
bst.add_node(10)
bst.add_node(0)

bst.print_inorder_traversal()




