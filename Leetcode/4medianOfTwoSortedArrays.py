class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Swap the arrays so that nums1 is shorter than nums2
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        x = len(nums1)
        y = len(nums2)
        
        low = 0
        high = x
        
        while low <= high:
            # Get index where we'll do the partition
            partitionX = (low + high) // 2
            partitionY = (x + y + 1)//2 - partitionX
            
            # For nums1: if partition is 0, assign -infinity as maxLeft value
            if partitionX == 0:
                maxLeftX = -sys.maxsize
            else:
                maxLeftX = nums1[partitionX-1]
            
            # If partition is the last element assign infinity as the minRight value
            if partitionX == x:
                minRightX = sys.maxsize
            else:
                minRightX = nums1[partitionX]
            
            # Repeat above two steps for nums2 
            if partitionY == 0:
                maxLeftY = -sys.maxsize
            else:
                maxLeftY = nums2[partitionY-1]
            
            if partitionY == y:
                minRightY = sys.maxsize
            else:
                minRightY = nums2[partitionY]

            # Check if both element in left side are lesser than the right side => parition is correct
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y)%2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return (max(maxLeftX, maxLeftY))
            
            # if macLeftX is greater => too many elements in maxLeftX, so reduce the count
            elif maxLeftX >= minRightY:
                high = partitionX -1
            
            # we are too far on left side for partitionX, go on right side 
            else:
                low = partitionX + 1
                    