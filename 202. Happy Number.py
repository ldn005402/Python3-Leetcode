class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def sqsum(num):
            res = 0
            while num > 0:
                r = num % 10
                res += r * r
                num /= 10
            return res
        
        rec = set()
        while sqsum(n) not in rec:
            summ = sqsum(n)
            if summ == 1:
                return True
            else:
                rec.add(summ)
                n = summ
        return False
