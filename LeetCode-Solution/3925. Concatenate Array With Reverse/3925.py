class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        
        ans = nums.copy()
        ans.extend(nums[::-1])
        return ans