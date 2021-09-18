class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def recurse(idx, val, prev_val, ops):
            if idx == len(num):
                if val == target:
                    res.append("".join(ops))
            else:
                curr_val = 0
                for i in range(idx, len(num)):
                    curr_val = 10*curr_val + int(num[i])
                    if idx == 0:
                        recurse(i+1, curr_val, curr_val, ops+[str(curr_val)])
                    else:
                        v = val - prev_val
                        recurse(i+1, v+prev_val*curr_val, prev_val*curr_val, ops+["*"+str(curr_val)])
                        recurse(i+1, val+curr_val, curr_val, ops+["+"+str(curr_val)])
                        recurse(i+1, val-curr_val, -curr_val, ops+["-"+str(curr_val)])
                    if num[idx] == "0":
                        break
        res = []
        recurse(0, 0, 0, [])
        return res
