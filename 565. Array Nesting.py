class Solution:
    def arrayNesting(self, nums):
        n = len(nums)
        visited = [0]*n
        for i in range(n):
            start, depth = i, 1
            while not visited[start]:
                visited[start] = depth
                start = nums[start]
                depth += 1
                
        return max(visited)
