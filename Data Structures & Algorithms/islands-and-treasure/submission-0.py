class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        (ROWS, COLS) = (len(grid), len(grid[0]))
        DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def isValid(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS

        def getNeighbors(row, col):
            neighbors = []
            for (d_r, d_c) in DIRS:
                (n_r, n_c) = (d_r+row, d_c+col)
                if isValid(n_r, n_c) and grid[n_r][n_c] != -1:
                    neighbors.append((n_r, n_c))
            return neighbors


        def bfs():
            distance = 0
            while queue:
                q_len = len(queue)
                for i in range(q_len):
                    (c_r, c_c) = queue.popleft()
                    grid[c_r][c_c] = distance
                    for (n_r, n_c) in getNeighbors(c_r, c_c):
                        if (n_r, n_c) not in seen:
                            seen.add((n_r, n_c))
                            queue.append((n_r, n_c))
                distance += 1

        seen = set()
        queue = collections.deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    seen.add((i, j))
                    queue.append((i, j))

        bfs()
        