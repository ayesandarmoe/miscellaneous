"""
 Reverse a doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def Reverse(head):
    
    if ( head == None):
        return None
    else:
        head.prev, head.next = head.next, head.prev
        if head.prev == None:
            return head
        else:
            return Reverse(head.prev)
        
  
   
  
  
  
  
  
  
