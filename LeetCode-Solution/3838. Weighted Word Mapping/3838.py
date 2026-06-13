from string import ascii_lowercase

class Solution:
    def mapWordWeights(self, words, weights):
        ans = []
        for word in words:
            s = sum(weights[ord(c) - ord('a')] for c in word)
            ans.append(ascii_lowercase[25 - s % 26])
        return ''.join(ans)