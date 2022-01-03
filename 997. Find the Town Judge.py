class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N==1:
            return 1
        ans = []
        for i in range(len(trust)):
            ans.append(trust[i][1])
        counts = collections.Counter(ans)
        y = sorted(ans, key=counts.get, reverse=True)[0]
        for i in range(len(trust)):
            if trust[i][0] == y:
                return -1
        return y
