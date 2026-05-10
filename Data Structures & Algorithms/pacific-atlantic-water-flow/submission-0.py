class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        pacific_ocean_nodes = []
        atlantic_ocean_nodes = []

        (ROWS, COLS) = (len(heights), len(heights[0]))

        for i in range(COLS):
            pacific_ocean_nodes.append((0, i))
            atlantic_ocean_nodes.append((ROWS-1, i))
            
        for i in range(ROWS):
            pacific_ocean_nodes.append((i, 0))
            atlantic_ocean_nodes.append((i, COLS-1))

        def isValid(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS

        def getNeighbors(row, col):
            neighbors = []

            for (dr, dc) in DIRS:
                (nr, nc) = (dr+row, dc+col)
                if isValid(nr, nc) and heights[nr][nc] >= heights[row][col]:
                    neighbors.append((nr, nc))
            return neighbors

        def dfs(nodes):
            seen = set()
            stack = []
            for (r, c) in nodes:
                if (r, c) not in seen:
                    seen.add((r, c))
                    stack.append((r, c))

            while stack:
                (c_r, c_c) = stack.pop()
                for (n_r, n_c) in getNeighbors(c_r, c_c):
                    if (n_r, n_c) not in seen:
                        seen.add((n_r, n_c))
                        stack.append((n_r, n_c))

            return seen

        pacific_reacheable_nodes = dfs(pacific_ocean_nodes)
        atlantic_reacheable_nodes = dfs(atlantic_ocean_nodes)

        return list(pacific_reacheable_nodes.intersection(atlantic_reacheable_nodes))
        

        
            
