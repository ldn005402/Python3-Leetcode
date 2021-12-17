class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
 
        record = {'b':1,'a':1,'l':2,'o':2,'n':1}
        
        h= {'b':0,'a':0,'l':0,'o':0,'n':0}
        
        for i in text:
                
            if i in h:
                h[i] += 1
        
        
        return min(h[i]//record[i] for i in h)
