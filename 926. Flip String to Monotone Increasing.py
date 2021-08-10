class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        c_ones = 0
        result = 0
        for i in S:
            if i == '0':
                """
                 I have two choices :
                 a) to either convert this element to 1 and check for the monotonicity of the remaining elements.It is 1(for this element  conversion) + result 
								 or
                 b) convert all the subsequent 1s to 0. This is basically the count of 1s in the array
                """
                result = min(1+ result,c_ones)
            else:
                c_ones +=1 
        return result 
