class Solution(object):
    def minCostToMoveChips(self, chips):
        odd , even = 0 ,0
        for i in chips:
            if i%2 ==0:
                even += 1
            else:
                odd += 1
        return min(even,odd)
