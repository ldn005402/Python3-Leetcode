class Solution:
    def maxPower(self, s: str) -> int:
        ans=1
        c=1
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                c+=1
            else:
                ans=max(ans,c)
                c=1
        ans=max(ans,c)
        return(ans)
