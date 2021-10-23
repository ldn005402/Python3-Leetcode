class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary Search
        left, right = 0, len(nums) - 1
        while left < right - 1:
            middle = (left + right) // 2
            # When left pointer needs to be changed
            if nums[middle] > nums[right]:
                left = middle
            # When right pointer needs to be changed
            else:
                # nums[middle] <= nums[left]
                # nums[left] < nums[middle] < nums[right]
                # nums[middle] == nums[right] (special handling: eliminate right)
                right = middle if nums[middle] != nums[right] else right - 1
        return nums[left] if nums[left] < nums[right] else nums[right]
