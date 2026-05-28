
MAX_VAL = 100
is_prime = [True] * (MAX_VAL + 1)
is_prime[0] = is_prime[1] = False  

i = 2
while i * i <= MAX_VAL:
    if is_prime[i]:
        
        for j in range(i * i, MAX_VAL + 1, i):
            is_prime[j] = False
    i += 1


class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        
       
        while l < r and not is_prime[nums[l]]:
            l += 1
            
       
        while l < r and not is_prime[nums[r]]:
            r -= 1
            
        
        return r - l