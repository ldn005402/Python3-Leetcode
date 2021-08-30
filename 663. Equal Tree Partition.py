class Solution(object):
    def checkEqualTree(self, root):
        memo = set()

        def subsum(node):
            if not node:
                return 0
            temp = node.val + subsum(node.left) + subsum(node.right)
            if node != root:
                memo.add(temp)
            return temp

        res = subsum(root)
        return False if res & 1 else res/2 in memo
