class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            res = set()
            for i in row:
                if i is not '.':
                    if i in res:
                        return False
                    else:
                        res.add(i)
        
        for col in zip(*board):
            res = set()
            for i in col:
                if i is not '.':
                    if i in res:
                        return False
                    else:
                        res.add(i)
        
        index = [(0,3),(3,6),(6,9)]  # range不包含右边界
        for i in range(3):
            for j in range(3):
                res = set()
                for m in range(*index[i]):
                    for n in range(*index[j]):
                        if board[m][n] is not '.':
                            if board[m][n] in res:
                                return False
                            else:
                                res.add(board[m][n])
        return True
