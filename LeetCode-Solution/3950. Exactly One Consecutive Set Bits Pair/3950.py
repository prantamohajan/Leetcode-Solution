class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        return (n & n >> 1).bit_count() == 1