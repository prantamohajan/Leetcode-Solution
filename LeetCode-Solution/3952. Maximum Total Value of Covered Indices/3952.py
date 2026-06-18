class Solution:
    def maxTotal(self, A: list[int], s: str) -> int:
        n = len(A)
        res = i = 0

        while i < n:
            if s[i] == '0':
                i += 1
                continue

            start = i - 1 if i > 0 else i
            j = i
            
            current_sum = 0
            current_min = float('inf')
            
            if i > 0:
                val = A[start]
                current_sum += val
                if val < current_min:
                    current_min = val
            
            while j < n and s[j] == '1':
                val = A[j]
                current_sum += val
                if val < current_min:
                    current_min = val
                j += 1

            if i > 0:
                current_sum -= current_min
                
            res += current_sum
            i = j
        
        return res