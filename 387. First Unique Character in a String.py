class Solution(object):
    "define a function of first unique chararter"
    def firstUniqChar(self, s):
        "set a dictionary"
        d = {}
        "loop every single chararter c in string s"
        for c in s:
            "start from the first letter, if not find, set it 0, next + 1"
            if c not in d:
                d[c] = 0
            d[c] += 1 
        "loop every charater c in string s, find the fist unique c, return its index"    
        for c in s:
            if d[c] == 1:
                return s.index(c)
        "if it doesnt exist, return -1"
        return -1
