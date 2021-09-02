class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        
        
        #current sum, number of nodes, max average
        
        def dfs(node):
            if not node:
                return 0, 0, 0
            left = dfs(node.left)
            right = dfs(node.right)
            curr_sum = left[0]+right[0]+node.val
            number_of_nodes = left[1]+right[1]+1
            max_average = max(left[2], right[2], curr_sum/(1+left[1]+right[1]))
            return curr_sum, number_of_nodes, max_average
        return dfs(root)[2]
