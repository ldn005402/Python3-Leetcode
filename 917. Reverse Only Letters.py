class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = list(S)
        l, r = 0, len(S) - 1

        while l < r:
            if not S[l].isalpha():
                l += 1
            elif not S[r].isalpha():
                r -= 1
            else:
                S[l], S[r] = S[r], S[l]
                l += 1
                r -= 1
        return ''.join(S)
