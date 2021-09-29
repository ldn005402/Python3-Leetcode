class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {0:-1}
        summ = 0
        maxlen = 0
        for i in range(len(nums)):
            summ += nums[i]
            if summ - k in dic and i-dic[summ-k] > maxlen:
                maxlen = i-dic[summ-k]
            if summ not in dic:
                dic[summ] = i
        return maxlen
