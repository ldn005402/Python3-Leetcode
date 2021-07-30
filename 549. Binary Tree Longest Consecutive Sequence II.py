class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0, 0
            elif not root.left and not root.right: 
                self.maxlen = max(self.maxlen, 1)
                return 1, 1
            l1, l2 = dfs(root.left)
            r1, r2 = dfs(root.right)
            if root.left:
                if root.left.val == root.val - 1:
                    l1 += 1
                    l2 = 1
                elif root.left.val == root.val + 1:
                    l2 += 1
                    l1 = 1
                else:
                    l1, l2 = 1, 1
            if root.right:
                if root.right.val == root.val - 1:
                    r1 += 1
                    r2 = 1
                elif root.right.val == root.val + 1:
                    r2 += 1
                    r1 = 1
                else:
                    r1, r2 = 1, 1
            if root.left and root.right:
                if root.left.val == root.val - 1 and root.right.val == root.val + 1:
                    self.maxlen = max(self.maxlen, l1+r2-1, l2, r1)
                elif root.left.val == root.val + 1 and root.right.val == root.val - 1:
                    self.maxlen = max(self.maxlen, l2+r1-1, l1, r2)
            self.maxlen = max(self.maxlen, l1, r1, l2, r2)
            return max(l1, r1), max(l2, r2)

        self.maxlen = 0
        dfs(root)
        return self.maxlen
