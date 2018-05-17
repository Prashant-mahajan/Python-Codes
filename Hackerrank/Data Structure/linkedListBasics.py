"""
 Print elements of a linked list on console
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 
"""

# Print elements of Linked List
def print_list(head):
    while head: 
        print(head.data)
        head = head.next
        
# Inserting new node to the linked list 

def Insert(head, data):
    if head == None:
        return Node(data,None)
    elif head.next == None:
        head.next = Node(data, None)
    else: 
        Insert(head.next, data)
    return head
    