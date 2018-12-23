# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA, lenB = self.listLen(headA), self.listLen(headB)
        if lenA > lenB:
            for i in range(lenA - lenB):
                headA = headA.next
        else:
            for i in range(lenB - lenA):
                headB = headB.next
        
        while(headA != headB):
            headA, headB = headA.next, headB.next
 
        return headA
                
                
    def listLen(self, head):
        count = 0
        while head:
            head = head.next
            count += 1
        return count
                
        