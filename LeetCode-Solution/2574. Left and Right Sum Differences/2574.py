class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        left_sum = 0
        right_sum = sum(nums)
        result = []
        for num in nums:
            right_sum -= num
            result.append(abs(left_sum - right_sum))
            left_sum += num
        return result
