class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        val = 1
        while val < n:
            val *= 2
            if val == n:
                return True
        return False
