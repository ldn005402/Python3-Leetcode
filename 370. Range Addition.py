class Solution:
    def getModifiedArray(self, length: 'int', updates: 'List[List[int]]') -> 'List[int]':
        
        start = collections.defaultdict(int)
        end = collections.defaultdict(int)
        for update in updates:
            sIdx, eIdx, val = update
            start[sIdx] += val
            end[eIdx] += val
            
        res = [0]*length
        Inc = 0  
        for i in range(length):
            if i in start:
                Inc += start[i]
            res[i] += Inc
            if i in end:
                Inc -= end[i]
        return res
