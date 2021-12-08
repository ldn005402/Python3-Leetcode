class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0, 0
            l = dfs(root.left)
            r = dfs(root.right)
            tilt = abs(l[1]-r[1])
            return l[0]+r[0]+tilt,l[1]+r[1]+root.val
        return dfs(root)[0]
