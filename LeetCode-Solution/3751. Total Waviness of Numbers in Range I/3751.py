from functools import cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def count_up_to(X: int) -> int:
            if X < 100:  
                return 0
            
            s = str(X)
            n = len(s)
            
            @cache
            def dp(i, prev1, prev2, waviness_count, is_less, is_started):
                if i == n:
                    return waviness_count
                
                limit = 9 if is_less else int(s[i])
                total = 0
                
                for d in range(limit + 1):
                    next_less = is_less or (d < limit)
                    
                    if not is_started:
                        if d == 0:
                            total += dp(i + 1, -1, -1, 0, next_less, False)
                        else:
                            total += dp(i + 1, d, -1, 0, next_less, True)
                    else:
                        new_waviness = 0
                        if prev2 != -1:
                            if (prev2 > prev1 and prev1 < d) or (prev2 < prev1 and prev1 > d):
                                new_waviness = 1
                        
                        total += dp(i + 1, d, prev1, waviness_count + new_waviness, next_less, True)
                        
                return total
            
            return dp(0, -1, -1, 0, False, False)
            
        return count_up_to(num2) - count_up_to(num1 - 1)