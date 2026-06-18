class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        ans = []
        current_chars = []
        
        def dfs(i, cost):
            if cost > k:
                return
            if i == n:
                ans.append("".join(current_chars))
                return
                
            current_chars.append("0")
            dfs(i + 1, cost)
            current_chars.pop()
            
            if not current_chars or current_chars[-1] == '0':
                current_chars.append("1")
                dfs(i + 1, cost + i)
                current_chars.pop()
                
        dfs(0, 0)
        return ans