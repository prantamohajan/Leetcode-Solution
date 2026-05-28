class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        lows = [-1] * 26
        ups = [-1] * 26
        for i, char in enumerate(word):
            
            if char.islower():
                lows[ord(char) - 97] = i
            
            elif char.isupper() and ups[ord(char) - 65] == -1:
                ups[ord(char) - 65] = i
        for i in range(26):
            if lows[i] != -1 and ups[i] > lows[i]:
                ans += 1
                
        return ans