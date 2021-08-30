class Solution:
    def maxCount(self, R, C, ops):
        if not ops: return R * C
        X, Y = zip(*ops)
        return min(X) * min(Y)   
