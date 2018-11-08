class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        array = [0]
        for i in range(1, num+1):
            array.append(array[i/2] + i%2)
        return array 


    # Normal method 
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        count = [0]
        array = []
        for i in range(1,num+1):
            array.append(self.convertBinary(i))
            count.append(array[i].count(1))

        return count
            
        
    def convertBinary(self,num):
        binary = []
        while num: 
            binary.append(num%2)
            num >>= 1
                
        return binary[::-1]
        
