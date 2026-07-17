class Solution:
    def processStr(self, s: str) -> str:
        ans = []
        for c in s:
            if 'a' <= c <= 'z':
                ans.append(c)
            elif c == '*':
                if ans:
                    ans.pop()
            elif c == '#':
                ans.extend(ans)
            elif c == '%':
                ans.reverse()
        return "".join(ans)