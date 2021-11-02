class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def isvalid(x, y): return 0 <= x < m and 0 <= y < n            
        def dfs(x, y, zeros_remaining):
            if zeros_remaining == 0:
                # find if there is end box
                for xx, yy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    if isvalid(x + xx, y + yy) and grid[x + xx][y + yy] == 2: self.path += 1
            else:
                # go to neighboring empty grid
                temp, grid[x][y] = grid[x][y], VISITED
                for xx, yy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    if isvalid(x + xx, y + yy) and grid[x + xx][y + yy] == 0: dfs(x + xx, y + yy, zeros_remaining - 1)
                grid[x][y] = temp
        
        m, n = len(grid), len(grid[0])
        
        # find start index, and count zeros
        zeros, startx, starty = 0, 0, 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1: startx, starty = r, c
                if grid[r][c] == 0: zeros += 1
				
        self.path, VISITED = 0, '#'
        dfs(startx, starty, zeros)
        return self.path
