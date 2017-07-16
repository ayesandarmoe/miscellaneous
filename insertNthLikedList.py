"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
    index = 0
    newNode = Node(data)
    
    # base case...it's an empty linked list
    if head == None:
        return newNode
    else:
        if position == 0:
            newNode.next = head
            head = newNode
        else:
            currentNode = head
            while( currentNode.next != None and index != position - 1  ):
                index = index + 1
                currentNode = currentNode.next
            newNode.next = currentNode.next
            currentNode.next = newNode

        return head
