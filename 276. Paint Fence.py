from math import factorial

class Solution:
    def numWays(self, n: int, k: int) -> int:
        total = 0
        twos, ones = divmod(n, 2)
        while twos >= 0:
            m = twos + ones
            cnt = factorial(twos+ones)//(factorial(twos)*factorial(ones))
            total += cnt * k * ((k-1) ** (m-1))
            twos -= 1; ones += 2
        return total
