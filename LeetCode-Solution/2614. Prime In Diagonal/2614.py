class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        
        def is_prime(n):
            if n <= 1:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            i = 3
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 2
            return True
        ans = 0
        n = len(nums)
        for i in range(n):
            val1 = nums[i][i]
            
            if val1 > ans and is_prime(val1):
                ans = val1
            val2 = nums[i][n - 1 - i]
            if val2 > ans and is_prime(val2):
                ans = val2
                
        return ans