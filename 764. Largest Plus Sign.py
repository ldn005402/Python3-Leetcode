class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        g = [[min(i, N-1-i, j, N-1-j) + 1 for j in range(N)] for i in range(N)]
        for (x, y) in mines:
            for i in range(N):
                g[i][y] = min(g[i][y], abs(i - x))
                g[x][i] = min(g[x][i], abs(i - y))
        return max([max(row) for row in g])
