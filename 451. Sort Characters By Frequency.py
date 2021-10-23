class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if s is None:
            return None
        
        stringDict = {}
        
        for x in s:
            if x in stringDict:
                stringDict[x] += 1 
            else:
                stringDict[x] = 1
                
                
      
        stringDictValueSorted = (sorted(stringDict.items(), key=lambda t:t[1]))
        print(stringDictValueSorted)
        stringAnswer = ""
        for (i,j) in stringDictValueSorted:
            part = i * j
            stringAnswer += part
            
        return stringAnswer[::-1]
        
