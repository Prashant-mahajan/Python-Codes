class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # To work in place instead of creating an separate matrix, assign 1->0 as 2 and 0->1 as 3 
        length, breadth = len(board), len(board[0])
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                count = 0

                # Works with neighbouring 8 elements in a matrix
                for a in range(max(0, i-1), min(i+2,length)):
                    for b in range(max(0, j-1), min(j+2, breadth)):
                        # If neighbouring element is 1 or 2 increase the count
                        if (a,b) != (i,j) and 1 <= board[a][b] <= 2: 
                            count += 1
                
                # Change the values (2 or 3) according to count         
                if board[i][j] == 0:
                    if count == 3: 
                        board[i][j] = 3
                else:
                    if count < 2 or count > 3:
                        board[i][j] = 2
        
        # Reassign according to required matrix
        for i in range(length):
            for j in range(breadth):
                if board[i][j] == 3:
                    board[i][j] = 1
                elif board[i][j] == 2:
                    board[i][j] = 0
                    

