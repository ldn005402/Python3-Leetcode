class Solution:
    def numDistinct(self, s, t):
        @lru_cache(None)
        def dp(i, j):
            if i == -1: return j == -1
            if j == -1: return j == -1
            return dp(i-1, j) + (s[i] == t[j]) * dp(i-1, j-1)
            
        return dp(len(s) - 1, len(t) - 1)
