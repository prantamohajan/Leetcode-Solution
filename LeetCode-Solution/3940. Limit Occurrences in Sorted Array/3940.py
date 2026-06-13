class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        i = 0
        for n in nums:
            if i < k or nums[i - k] != n:
                nums[i] = n
                i += 1
        return nums[:i]