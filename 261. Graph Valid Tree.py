class Solution(object):
    def root(self, i, components):
        while i != components[i]:
            i = components[i]
        return i
    
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        components = [i for i in range(n)]
        for edge in edges:
            u, v = edge[0], edge[1]
            root_u, root_v = self.root(u, components), self.root(v, components)
            if root_u == root_v:  # If an edge end points are in the same component, we have a cycle.
                return False
            else:
                components[root_u] = root_v
        return len(edges) == n - 1 # if the number of edges are not equal to n-1, then not a tree
