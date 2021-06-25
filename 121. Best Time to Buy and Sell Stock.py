class Solution:
    def maxProfit(self, prices: List[int]):
        m, mp = float('inf'), 0
        for p in prices:
            if p < m: m =p
            if p - m > mp: mp = p - m
        return mp
