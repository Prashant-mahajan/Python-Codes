# problem: https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem

"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def MergeLists(headA, headB):
    if headA == None and headB == None:
        return None

    if headA == None:
        return headB

    if headB == None:
        return headA

    if headA.data < headB.data: 
        headA.next = MergeLists(headA.next, headB)

    if headB.data < headA.data:
        tempNode = headB
        headB = headB.next
        tempNode.next = headA
        headA = tempNode
        headA.next = MergeLists(headA.next, headB)

    return headA