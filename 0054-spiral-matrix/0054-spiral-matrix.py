class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        i = 0
        j = -1

        m = len(matrix)      # remaining rows
        n = len(matrix[0])   # remaining cols

        dir = 1

        while m > 0 and n > 0:

            # move horizontally
            for _ in range(n):
                j += dir
                res.append(matrix[i][j])
            m -= 1

            # move vertically
            for _ in range(m):
                i += dir
                res.append(matrix[i][j])
            n -= 1

            dir = -dir   # reverse direction

        return res