class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        
        # Step 1: make a copy so we don't lose original values
        copy = [row[:] for row in board]
        
        # Step 2: loop through every cell
        for i in range(rows):
            for j in range(cols):
                live = 0  # count of live neighbours
                
                # Step 3: check all 8 directions (around the cell)
                for x in range(max(0, i - 1), min(rows, i + 2)):
                    for y in range(max(0, j - 1), min(cols, j + 2)):
                        if (x, y) != (i, j):  # skip itself
                            if copy[x][y] == 1:
                                live += 1
                
                # Step 4: apply the rules
                if copy[i][j] == 1:
                    if live < 2 or live > 3:
                        board[i][j] = 0  # dies
                    else:
                        board[i][j] = 1  # stays alive
                else:
                    if live == 3:
                        board[i][j] = 1  # dead -> live