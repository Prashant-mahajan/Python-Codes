    def insert(self,head,data): 
    #Complete this method
        if head == None:
            return Node(data)
        elif head.next == None:
            head.next = Node(data)
        else:
            self.insert(head.next,data)    
        return self.display(head) 