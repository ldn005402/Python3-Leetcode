class Solution:
    def minCut(self, s: str) -> int:
        if s == s[::-1]: return 0
        for i in range(1, len(s)):
            if s[:i]==s[:i][::-1] and s[i:]==s[i:][::-1]: return 1

        dp = [float('inf')] * (len(s)+1); dp[0] = -1
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    dp[j+1] = min(dp[j+1], dp[i]+1)
        return dp[-1]
