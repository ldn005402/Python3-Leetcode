class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        data = preorder.split(",")
        end = data.pop()
        if end != "#":
            return False
        stack = []
        for i in range(len(data)):
            char = data[i]
            if char != "#":
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    stack.pop()
        return not stack
