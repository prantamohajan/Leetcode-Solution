from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total_numbers = n * n
        
        seen = set()
        repeated = -1
        
        
        for row in grid:
            for num in row:
                if num in seen:
                    repeated = num
                seen.add(num)
                
        missing = -1
        for i in range(1, total_numbers + 1):
            if i not in seen:
                missing = i
                break
                
        return [repeated, missing]