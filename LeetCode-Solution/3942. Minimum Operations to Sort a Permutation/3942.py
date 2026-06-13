class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
            
        isA = True
        isB = True
        idx = 0
        
        for i in range(n - 1):
            if nums[i] == 0:
                idx = i
            diff = nums[i + 1] - nums[i]
            if diff != 1 and diff != 1 - n:
                isA = False
            if diff != -1 and diff != n - 1:
                isB = False
                
        if nums[n - 1] == 0:
            idx = n - 1
        diff = nums[0] - nums[n - 1]
        if diff != 1 and diff != 1 - n:
            isA = False
        if diff != -1 and diff != n - 1:
            isB = False
            
        ans = float('inf')
        
        if isA:
            if idx < ans:
                ans = idx
            alt = n - idx + 2
            if alt < ans:
                ans = alt
                
        if isB:
            v1 = n - idx
            v2 = idx + 2
            if v1 < ans:
                ans = v1
            if v2 < ans:
                ans = v2
                
        return -1 if ans == float('inf') else ans
        