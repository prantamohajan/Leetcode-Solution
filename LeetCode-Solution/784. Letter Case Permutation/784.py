from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = [""]
        
        for char in s:
            if char.isalpha():
                result = [string + char.lower() for string in result] + \
                        [string + char.upper() for string in result]
            else:
                result = [string + char for string in result]
                
        return result