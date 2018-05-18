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
    
# Inserting new node at the start of linked list

def Insert(head, data):
    NewNode = Node(data)
    NewNode.next = head
    head = NewNode
    return head

# Insert node at a particular position in a linked list 

def InsertNth(head, data, position):
    if position==0:
        return Node(data, head)
    top = head
    for _ in range(position-1):
        top = top.next
    NewNode = Node(data, top.next)
    top.next = NewNode
    return head

# Deleting a node in a linked list 
def Delete(head, position):
    if position == 0:
        head = head.next
        return head
    
    top = head
    for _ in range(position-1):
        top = top.next
    top.next = top.next.next

    return head