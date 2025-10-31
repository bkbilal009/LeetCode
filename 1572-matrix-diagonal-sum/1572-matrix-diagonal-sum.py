class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0
        for i in range(n):
            total += mat[i][i]           # primary diagonal
            total += mat[i][n - 1 - i]   # secondary diagonal
        
        # if matrix size is odd -> subtract middle element once
        if n % 2 == 1:
            total -= mat[n // 2][n // 2]
        
        return total