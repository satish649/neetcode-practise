class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        queue = deque()

        (ROWS, COLS) = (len(grid), len(grid[0]))

        total_fresh_fruits = 0
        seen = set()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    seen.add((i, j))
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    total_fresh_fruits += 1

        if total_fresh_fruits == 0:
            return 0
        
        def isValid(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS

        def getNeighbors(row, col):
            neighbors = []
            for (d_r, d_c) in DIRS:
                (n_r, n_c) = (d_r+row, d_c+col)
                if isValid(n_r, n_c) and grid[n_r][n_c] == 1:
                    neighbors.append((n_r, n_c))
            return neighbors

        minutes = -1
        rotten_fresh_fruits = 0
        while queue:
            q_len = len(queue)
            for _ in range(q_len):
                (r, c) = queue.popleft()
                for (n_r, n_c) in getNeighbors(r, c):
                    if (n_r, n_c) not in seen:
                        rotten_fresh_fruits += 1
                        seen.add((n_r, n_c))
                        queue.append((n_r, n_c))
            minutes += 1

        if rotten_fresh_fruits == total_fresh_fruits:
            return minutes
        else:
            return -1


        