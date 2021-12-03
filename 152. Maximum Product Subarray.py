class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N == 1:
            return nums[0]
        max_til_here = nums[0]
        min_til_here = nums[0]
        max_end_here = nums[0]
        min_end_here = nums[0]
        for i in range(1,N):
            lis = sorted([max_end_here*nums[i], min_end_here*nums[i], nums[i]])
            max_end_here = lis[-1]
            min_end_here = lis[0]
            if max_til_here < max_end_here:
                max_til_here = max_end_here
            if min_til_here > min_end_here:
                min_til_here = min_end_here
        return max_til_here
