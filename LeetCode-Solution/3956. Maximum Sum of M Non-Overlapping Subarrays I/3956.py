import math
from collections import deque
from typing import List

class Solution:
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
            
        INF = math.inf
        prev_dp = [0] * (n + 1)
        ans = -INF
        
        for j in range(1, m + 1):
            curr_dp = [-INF] * (n + 1)
            dq = deque()
            
            for i in range(l, n + 1):
                k = i - l
                val = prev_dp[k] - pref[k]
                
                if val != -INF:
                    while dq and dq[-1][1] <= val:
                        dq.pop()
                    dq.append((k, val))
                    
                while dq and dq[0][0] < i - r:
                    dq.popleft()
                    
                curr_dp[i] = curr_dp[i - 1]
                if dq:
                    val_with_pref = pref[i] + dq[0][1]
                    if val_with_pref > curr_dp[i]:
                        curr_dp[i] = val_with_pref
                        
            if curr_dp[n] > ans:
                ans = curr_dp[n]
            prev_dp = curr_dp
            
        return ans