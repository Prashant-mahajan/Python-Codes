    def removeDuplicates(self,head):
        #Write your code here
        if head.next == None:
            return head
        if head.data == head.next.data:
            return self.removeDuplicates(head.next)
        
        head.next = self.removeDuplicates(head.next)
        return head
            