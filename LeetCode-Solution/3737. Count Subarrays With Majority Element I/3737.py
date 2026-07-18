class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        converted = [1 if x == target else -1 for x in nums]
        
        count = 0
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += converted[j]
                if total > 0:
                    count += 1
        return count