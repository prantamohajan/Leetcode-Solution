from typing import List

class Solution:
    def countValidSubsets(self, parent: List[int], nums: List[int], k: int) -> int:
        n = len(parent)
        MOD = 10**9 + 7
        
        dp0 = [[0] * k for _ in range(n)]
        dp1 = [[0] * k for _ in range(n)]
        
        for i in range(n):
            dp0[i][0] = 1
            dp1[i][nums[i] % k] = 1
            
        for v in range(n - 1, 0, -1):
            u = parent[v]
            
            next_dp0 = [0] * k
            next_dp1 = [0] * k
            
            child_total = [(dp0[v][r] + dp1[v][r]) % MOD for r in range(k)]
            
            for r_u in range(k):
                if dp0[u][r_u] == 0:
                    continue
                for r_v in range(k):
                    if child_total[r_v] == 0:
                        continue
                    r_next = (r_u + r_v) % k
                    next_dp0[r_next] = (next_dp0[r_next] + dp0[u][r_u] * child_total[r_v]) % MOD
                    
            for r_u in range(k):
                if dp1[u][r_u] == 0:
                    continue
                for r_v in range(k):
                    if dp0[v][r_v] == 0:
                        continue
                    r_next = (r_u + r_v) % k
                    next_dp1[r_next] = (next_dp1[r_next] + dp1[u][r_u] * dp0[v][r_v]) % MOD
                    
            dp0[u] = next_dp0
            dp1[u] = next_dp1
            
        ans = (dp0[0][0] + dp1[0][0] - 1 + MOD) % MOD
        return ans