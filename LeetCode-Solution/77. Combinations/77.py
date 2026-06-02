from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtrack(start: int, current_combo: List[int]):
            if len(current_combo) == k:
                result.append(list(current_combo))
                return
            upper_bound = n - (k - len(current_combo)) + 1
            for i in range(start, upper_bound + 1):
                current_combo.append(i)
                backtrack(i + 1, current_combo)
                current_combo.pop()
                
        backtrack(1, [])
        return result