
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        n1 = ""
        n2 = ""
      
        curr = l1
        while curr:
          n1+= str(curr.val)  
          curr = curr.next
        
        curr = l2
        while curr:
          n2+= str(curr.val)
          curr = curr.next
        
       
        result = str(int(n1[::-1]) + int(n2[::-1]))
        result = result[::-1]
        
        lista = ListNode(result[0])
        head = lista
        
        for i in range(1,len(result)):
          while head.next:
            head = head.next
          head.next = ListNode(result[i], None)
            
        return lista
            
        
            
        