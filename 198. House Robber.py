class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        prev = 0
        curr = 0
        for n in nums:
            prev, curr = curr, max(prev + n, curr)
        return curr
