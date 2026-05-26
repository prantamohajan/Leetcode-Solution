class Solution:
    def passwordStrength(self, password: str) -> int:
        uniqueChars = set(password)
        totalStrength = 0
        
        
        has_lower = False
        has_upper = False
        has_digit = False
        has_special = False
        
        special_chars = {"!", "@", "#", "$"}
        
        for char in uniqueChars:
            if char.islower() and not has_lower:
                totalStrength += 1
                has_lower = True
            elif char.isupper() and not has_upper:
                totalStrength += 2
                has_upper = True
            elif char.isdigit() and not has_digit:
                totalStrength += 3
                has_digit = True
            elif char in special_chars and not has_special:
                totalStrength += 5
                has_special = True
                
        return totalStrength