class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        dp = [0] * length
        
        dp[0] = nums[0]
        
        for i in range(1, length - 1):
            
            if dp[i - 1] < i:
                return False
            
            dp[i] = max(i + nums[i], dp[i - 1])
            
            if dp[i] >= length - 1:
                return True
        
        return dp[length - 2] >= length - 1
