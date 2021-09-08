class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        r, c = len(grid), len(grid[0])
        sumr = [i for i in range(r) for j in range(c) if grid[i][j]]
        sumc = [j for i in range(r) for j in range(c) if grid[i][j]]
        
        if len(sumr) % 2 == 0:
            midrow = self.medianEven(sumr)
        else:
            midrow = self.medianOdd(sumr)
        
        if len(sumc) % 2 == 0:
            midcol = self.medianEven(sumc)
        else:
            midcol = self.medianOdd(sumc)
            
        rowpoint = sum([abs(r-midrow) for r in sumr])
        colpoint = sum([abs(c-midcol) for c in sumc])
        
        return int(rowpoint + colpoint)
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) % 2 == 0:
            median = self.medianEven(nums)
        else:
            median = self.medianOdd(nums)
        #print(median)
        moves = 0
        for num in nums:
            moves += abs(num - median)
        return int(moves)
        
    def findKlargest(self, arr, k):
        k = len(arr)-k
        left = 0
        right = len(arr)-1
        random.shuffle(arr)
        while left <= right:
            pivot = self.findPivotIndex(arr, left, right)

            if pivot == k:
                return arr[pivot]
            elif pivot > k:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1


    def findPivotIndex(self, arr, low, high):
        pivot = arr[high]
        i = low

        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i+=1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    def medianEven(self, arr):
        n = len(arr)
        l = self.findKlargest(arr, n // 2 + 1)
        r = self.findKlargest(arr, n // 2)
        return float((l+r)/2.0)

    def medianOdd(self, arr):
        n = len(arr)
        l = self.findKlargest(arr, n // 2 + 1)
        return l
