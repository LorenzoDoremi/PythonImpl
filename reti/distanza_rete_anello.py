class LinkedList():
    def __init__(self, id):
        self.id = id
        self.next = None
        # lista concatenata bidirezionale
        self.before = None
     
     
    # distanza tra nodo radice e un nodo target 
    def traverse(self, target, d):
        if(self.id == target):
            return d
        elif(self.next):
            return self.next.traverse(target,d+1)
       
    
'''
calcola la distanza tra due nodi
'''

root = LinkedList(0)
curr = root
for i in range(1,10):
    curr.next = LinkedList(i)
    # lista concatenata bidirezionale
    curr.next.before = curr
    curr = curr.next
    
    


    
    
print(root.traverse(5,0))