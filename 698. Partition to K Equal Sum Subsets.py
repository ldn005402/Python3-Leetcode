class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        nums.sort(reverse=True) # Game Changer 1
        buck, kSum = [0] * k, sum(nums) // k
        def dfs(idx):
            if idx == len(nums): return len(set(buck)) == 1
            for i in range(k):
                buck[i] += nums[idx]
                if buck[i] <= kSum and dfs(idx + 1): return True
                buck[i] -= nums[idx]
                if buck[i] == 0: break # Game Changer 2
            return False
        return dfs(0)
