class Solution:
    def customSortString(self, S: str, T: str) -> str:        
        counter =collections.Counter(T)
        res = []
        for i in S:
            if i in counter:
                res.extend([i]*counter[i])
                counter.pop(i)
        for k,v in counter.items():
            res.extend(k*v)
        return ''.join(res)
