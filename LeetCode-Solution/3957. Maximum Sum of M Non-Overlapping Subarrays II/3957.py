import math
from collections import deque
from typing import List

class Solution:
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
            
        max_single = -math.inf
        dq_single = deque()
        for i in range(l, n + 1):
            k = i - l
            val = -pref[k]
            while dq_single and dq_single[-1][1] <= val:
                dq_single.pop()
            dq_single.append((k, val))
            while dq_single and dq_single[0][0] < i - r:
                dq_single.popleft()
            
            cand = pref[i] + dq_single[0][1]
            if cand > max_single:
                max_single = cand
            
        if max_single <= 0:
            return int(max_single)
            
        def check(cost):
            dp_val = [0] * (n + 1)
            dp_cnt = [0] * (n + 1)
            dq = deque()
            
            for i in range(l, n + 1):
                k = i - l
                val_k = dp_val[k] - pref[k]
                cnt_k = dp_cnt[k]
                
                while dq:
                    last = dq[-1]
                    if last[0] < val_k or (last[0] == val_k and last[1] <= cnt_k):
                        dq.pop()
                    else:
                        break
                dq.append((val_k, cnt_k, k))
                
                limit = i - r
                while dq and dq[0][2] < limit:
                    dq.popleft()
                    
                dp_val[i] = dp_val[i - 1]
                dp_cnt[i] = dp_cnt[i - 1]
                
                if dq:
                    best_val, best_cnt, _ = dq[0]
                    cand_val = pref[i] + best_val - cost
                    cand_cnt = best_cnt + 1
                    
                    if cand_val > dp_val[i]:
                        dp_val[i] = cand_val
                        dp_cnt[i] = cand_cnt
                    elif cand_val == dp_val[i] and cand_cnt > dp_cnt[i]:
                        dp_cnt[i] = cand_cnt
                        
            return dp_val[n], dp_cnt[n]
            
        val0, cnt0 = check(0)
        if cnt0 <= m:
            return val0
            
        low = 0
        high = 2000000000000000
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            val, cnt = check(mid)
            
            if cnt >= m:
                ans = val + m * mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans