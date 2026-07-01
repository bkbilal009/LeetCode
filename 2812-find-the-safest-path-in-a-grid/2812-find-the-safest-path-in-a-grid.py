from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        
        # Directions for moving up, down, left, right
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Initialize distances grid with infinity
        distances = [[float('inf')] * C for _ in range(R)]
        q = deque()
        
        # Find all thieves and add them to the queue
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    distances[r][c] = 0
                    q.append((r, c))
                    
        # Multi-source BFS to calculate safeness factor for each cell
        while q:
            x, y = q.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C:
                    if distances[nx][ny] == float('inf'):
                        distances[nx][ny] = distances[x][y] + 1
                        q.append((nx, ny))
                        
        # Binary Search to find the maximum possible safeness factor for a path
        def good(target):
            if distances[0][0] < target:
                return False
                
            q = deque([(0, 0)])
            seen = {(0, 0)}
            
            while q:
                x, y = q.popleft()
                if x == R - 1 and y == C - 1:
                    return True
                    
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < R and 0 <= ny < C:
                        if distances[nx][ny] >= target and (nx, ny) not in seen:
                            seen.add((nx, ny))
                            q.append((nx, ny))
            return False

        left = 0
        right = R * C # Safe upper bound for binary search
        
        while left < right:
            mid = (left + right + 1) // 2
            if good(mid):
                left = mid
            else:
                right = mid - 1
                
        return left