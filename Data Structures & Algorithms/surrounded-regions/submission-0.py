class Solution:
    def solve(self, board: List[List[str]]) -> None:

        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        border_regions = set()

        (ROWS, COLS) = (len(board), len(board[0]))
        seen = set()

        for i in range(COLS):
            if board[0][i] == "O":
                border_regions.add((0, i))
                seen.add((0, i))
            if board[ROWS-1][i] == 'O':
                border_regions.add((ROWS-1, i))
                seen.add((ROWS-1, i))
        
        for i in range(ROWS):
            if board[i][0] == "O":
                border_regions.add((i, 0))
                seen.add((i, 0))
            if board[i][COLS-1] == "O":
                border_regions.add((i, COLS-1))
                seen.add((i, COLS-1))

        def isValid(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS

        def getNeighbors(row, col):
            neighbors = []
            for (dr, dc) in DIRS:
                (nr, nc) = (dr+row, dc+col)
                if isValid(nr, nc) and board[nr][nc] == "O":
                    neighbors.append((nr, nc))
            return neighbors

        stack = list(border_regions)
        while stack:
            (r, c) = stack.pop()
            for (nr, nc) in getNeighbors(r, c):
                if (nr, nc) not in seen:
                    seen.add((nr, nc))
                    stack.append((nr, nc))
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O" and (i, j) not in seen:
                    board[i][j] = 'X'



        


        