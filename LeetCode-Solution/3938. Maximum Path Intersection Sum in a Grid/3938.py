class Solution:
    def maxScore(self, g: List[List[int]]) -> int:
        m = len(g)
        n = len(g[0])

        a = float("-inf")
        i = 0

        while i < m:
            c = g[i][0] + g[i][1]
            a = max(a, c)
            j = 2

            while j < n:
                c = max(c + g[i][j], g[i][j - 1] + g[i][j])
                a = max(a, c)
                j += 1

            i += 1

        j = 0
        while j < n:
            c = g[0][j] + g[1][j]
            a = max(a, c)
            i2 = 2

            while i2 < m:
                c = max(c + g[i2][j], g[i2 - 1][j] + g[i2][j])
                a = max(a, c)
                i2 += 1

            j += 1

        i = 1
        while i < m - 1:
            j = 1
            while j < n - 1:
                a = max(a, g[i][j])
                j += 1

            i += 1

        return a