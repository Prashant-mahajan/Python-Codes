"""
 Merge two linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def CompareLists(headA, headB):
    while(headA and headB):
        if headA.data == headB.data:
            headA = headA.next
            headB = headB.next
        else:
            return 0
    if (headA and not headB or headB and not headA):
        return 0    
    return 1