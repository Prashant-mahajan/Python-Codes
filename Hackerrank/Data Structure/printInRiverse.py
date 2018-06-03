"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def ReversePrint(head):
    values = []
    top = head
    while(top):
        values.append(top.data)
        top = top.next
        
    for i in reversed(values):
        print (i)
        

# Using Recursive function 

def ReversePrint(head):
    if head == None:
        return
    else:
        ReversePrint(head.next)
        print(head.data)
         