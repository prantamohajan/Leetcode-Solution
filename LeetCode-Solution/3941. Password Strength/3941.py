class Solution:
    def passwordStrength(self, password: str) -> int:
        uniqueChars = set(password)
        totalStrength = 0
        
        special_chars = {"!", "@", "#", "$"}
        for char in uniqueChars:
            if char.islower():
                totalStrength += 1
            elif char.isupper():
                totalStrength += 2
            elif char.isdigit():
                totalStrength += 3
            elif char in special_chars:
                totalStrength += 5
                
        return totalStrength