class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        return sum(p for p in range(max(1, n - k), n + k + 1) if (n & p) == 0)