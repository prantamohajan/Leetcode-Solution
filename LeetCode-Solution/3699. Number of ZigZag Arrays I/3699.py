class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1000000007
        p = r - l + 1
        dp = [1] * p

        for i in range(2, n + 1):
            dp.reverse()
            s = 0
            for j in range(p):
                dp[j], s = s, (s + dp[j]) % MOD

        return (sum(dp) % MOD << 1) % MOD