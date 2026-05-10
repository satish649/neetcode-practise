class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        (ROWS, COLS) = (len(grid), len(grid[0]))

        DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        seen = set()
        
        def isValid(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS

        def getNeighbors(row, col):
            neighbors = []

            for (d_r, d_c) in DIRS:
                (n_r, n_c) = (d_r+row, d_c+col)
                if isValid(n_r, n_c) and grid[n_r][n_c] == 1:
                    neighbors.append((n_r, n_c))
            return neighbors

        def dfs(row, col):
            stack = [(row, col)]
            seen.add((row, col))

            connected_nodes = 0
            while stack:
                (c_r, c_c) = stack.pop()
                connected_nodes += 1

                for (n_r, n_c) in getNeighbors(c_r, c_c):
                    if (n_r, n_c) not in seen:
                        seen.add((n_r, n_c))
                        stack.append((n_r, n_c))

            return connected_nodes

        max_area = 0 # assume there are no islands to start with
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in seen:
                    max_area = max(dfs(i, j), max_area)
        
        return max_area




        