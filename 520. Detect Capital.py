class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # All letters are capital
        if all([ord("Z")>=ord(word[i])>=ord("A") for i in range(len(word))]):
            return True
        
        # If capital letters appear not in the first place
        for letter in word[1:]:
            if ord("Z")>=ord(letter)>=ord("A"):
                return False
        
        return True
