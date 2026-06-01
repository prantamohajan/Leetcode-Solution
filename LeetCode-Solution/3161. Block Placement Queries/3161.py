import bisect

class FenwickTree:
    def __init__(self, n):
        self.tree = [0] * (n + 1)
        self.size = n

    def maximize(self, i, val):
        while i <= self.size:
            if val > self.tree[i]:
                self.tree[i] = val
            else:
                break  
            i += i & (-i)

    def query(self, i):
        max_val = 0
        while i > 0:
            if self.tree[i] > max_val:
                max_val = self.tree[i]
            i -= i & (-i)
        return max_val

class Solution:
    def getResults(self, queries: list[list[int]]) -> list[bool]:
    
        max_x = max(q[1] for q in queries)
        n = min(50000, max_x + 1)
        
        
        obstacles = [0, n]
        
        
        for q in queries:
            if q[0] == 1:
                bisect.insort(obstacles, q[1])
        
        
        bit = FenwickTree(n + 1)
        for i in range(1, len(obstacles)):
            gap = obstacles[i] - obstacles[i - 1]
            bit.maximize(obstacles[i], gap)
            
        ans = []
        
        
        for q in reversed(queries):
            q_type = q[0]
            x = q[1]
            
            if q_type == 1:
                idx = bisect.bisect_left(obstacles, x)
                prev_obs = obstacles[idx - 1]
                next_obs = obstacles[idx + 1]
                
                bit.maximize(next_obs, next_obs - prev_obs)
                
                obstacles.pop(idx)
            else:
                sz = q[2]
                
                idx = bisect.bisect_right(obstacles, x)
                prev_obstacle = obstacles[idx - 1]
                if bit.query(prev_obstacle) >= sz or (x - prev_obstacle) >= sz:
                    ans.append(True)
                else:
                    ans.append(False)
                    
        return ans[::-1]