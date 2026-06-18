class Solution:
    def maximumMEX(self, nums: list[int]) -> list[int]:
        n = len(nums)
        suf = [0] * n
        s = [0] * (n + 2)
        m = 0
        
        for i in range(n - 1, -1, -1):
            if nums[i] <= n:
                s[nums[i]] = 1
            while s[m]:
                m += 1
            suf[i] = m
            
        res = []
        c = [0] * (n + 2)
        i = 0
        mx = 0
        
        while i < n:
            tar = suf[i]
            j = i
            while j < n:
                if nums[j] <= n:
                    c[nums[j]] += 1
                while c[mx]:
                    mx += 1
                if mx == tar:
                    break
                j += 1
                
            res.append(tar)
            for k in range(i, j + 1):
                if nums[k] <= n:
                    c[nums[k]] -= 1
                    
            mx = 0
            i = j + 1
            
        return res