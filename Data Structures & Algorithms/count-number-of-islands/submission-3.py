class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        seen = set()

        def isValid(row, col):
            return 0 <= row < m and 0 <= col < n

        def getNeighbors(row, col):
            neighbors = []
            for (d_r, d_c) in dirs:
                (n_r, n_c) = (d_r + row, d_c + col)
                if isValid(n_r, n_c) and grid[n_r][n_c] == "1":
                    neighbors.append((n_r, n_c))
            return neighbors

        def dfsHelper(row, col):
            stack = [(row, col)]
            seen.add((row, col))

            while stack:
                (c_r, c_c) = stack.pop()
                for (n_r, n_c) in getNeighbors(c_r, c_c):
                    if (n_r, n_c) not in seen:
                        seen.add((n_r, n_c))
                        stack.append((n_r, n_c))

        island_cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in seen:
                    dfsHelper(i, j)
                    island_cnt += 1
        
        return island_cnt





        