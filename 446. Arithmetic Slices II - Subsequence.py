class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total = 0
        dp = [defaultdict(int) for i in nums]
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += dp[j][diff] + 1
                total += dp[j][diff]
        return total
