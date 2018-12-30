# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ans = []
        for head in lists:
            curr = head
            while curr is not None:
                ans.append(curr.val)
                curr = curr.next

        return(sorted(ans))
        
    # Using Priority Queue
#     def mergeKLists(self, lists):
#         start = pointer = ListNode(0)
#         q = PriorityQueue()
        
#         for a in lists:    
#             if a:
#                 q.put((a.val, a))
                
#             while not q.empty():
#                 val, node = q.get()
#                 pointer.next = ListNode(val)
#                 pointer = pointer.next
#                 node = node.next
                
#                 if node:
#                     q.put((node.val, node))
#         return start.next
    
    
                