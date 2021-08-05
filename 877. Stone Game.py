class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        self.mem = dict()
        def helper(l, r, is_alex, alex, lee):
            key = (l, r, is_alex)
            if key in self.mem:
                return self.mem[key]
            if l == r:
                lee += piles[l]
                if alex > lee:
                    self.mem[key] = True
                else:
                    self.mem[key] = False
                return self.mem[key]
            if is_alex:
                r1 = helper(l + 1, r, False, alex + piles[l], lee)
                r2 = helper(l, r - 1, False, alex + piles[r], lee)
            else:
                r1 = helper(l + 1, r, True, alex, lee + piles[l])
                r2 = helper(l, r - 1, True, alex, lee + piles[r])
            self.mem[key] = r1 or r2
            return self.mem[key]
        return helper(0, len(piles) - 1, True, 0, 0)
