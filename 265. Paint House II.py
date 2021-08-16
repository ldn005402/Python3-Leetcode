class Solution(object):
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        for i in range(1,len(costs)):
            for k in range(len(costs[0])):
                costs[i][k] += min(costs[i-1][:k]+costs[i-1][k+1:])
        return min(costs[-1])
