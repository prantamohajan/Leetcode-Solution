import random

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        def partition3(left, right):
            pivot = nums[random.randint(left, right)]
            lt, gt = left, right
            i = left
            while i <= gt:
                if nums[i] > pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] < pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1
            return lt, gt

        target = k - 1
        left, right = 0, len(nums) - 1
        while True:
            lt, gt = partition3(left, right)
            if target < lt:
                right = lt - 1
            elif target > gt:
                left = gt + 1
            else:
                return nums[target]