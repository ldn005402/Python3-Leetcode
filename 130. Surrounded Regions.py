class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board: return
        m, n = len(board), len(board[0])
        
        def fillN(i, j):
            if 0<=i<m and 0<=j<n and board[i][j] == "O":
                board[i][j] = "N"
                fillN(i+1, j)
                fillN(i-1, j)
                fillN(i, j+1)
                fillN(i, j-1)
            
        for i in range(m):
            if board[i][0] == "O": fillN(i,0)
            if board[i][n-1] == "O": fillN(i,n-1)        
        for j in range(n):
            if board[0][j] == "O": fillN(0,j)
            if board[m-1][j] == "O": fillN(m-1,j)
                
        for i in range(m):
            for j in range(n):
                if board[i][j] != "N": board[i][j] = "X"
                else: board[i][j] = "O"
