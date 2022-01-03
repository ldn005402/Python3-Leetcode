class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d = {}
        for i in trust:
            try:
                x = d[i[0]]
                x.append(i[1])
                d[i[0]] = x
            except KeyError:
                d[i[0]] = [i[1]]
        
        townjudgeCandidates = []
        for i in range(1,n+1):
            try:
                x = d[i]
            except KeyError:
                d[i] = []
                townjudgeCandidates.append(i)
        
        if len(townjudgeCandidates) == 0:
            return -1
        
        found = True
        for cand in townjudgeCandidates:
            for i in range(1,n+1):
                if i != cand:
                    if cand not in d[i]:
                        found = False
                        break
            if found == True:
                return cand
        if found == False:
            return -1
