class Solution:
    def maxScore(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        max_steps = m + n - 2
        
        dp = [[float('-inf')] * m for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        for step in range(1, max_steps + 1):
            next_dp = [[float('-inf')] * m for _ in range(m)]
            
            for r1 in range(min(step + 1, m)):
                for r2 in range(min(step + 1, m)):
                    c1 = step - r1
                    c2 = step - r2
                    
                    if c1 >= n or c2 >= n:
                        continue
                    current_sum = grid[r1][c1] if r1 == r2 else grid[r1][c1] + grid[r2][c2]
                    
                    prev_max = float('-inf')
                    for p1 in [r1 - 1, r1]:
                        for p2 in [r2 - 1, r2]:
                            if p1 >= 0 and p2 >= 0:
                                prev_max = max(prev_max, dp[p1][p2])
                                
                    if prev_max != float('-inf'):
                        next_dp[r1][r2] = prev_max + current_sum
                        
            dp = next_dp
            
        return max(0, dp[m - 1][m - 1])