class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        value = max(nums)
        total = min(nums)
        return (value - total)* k