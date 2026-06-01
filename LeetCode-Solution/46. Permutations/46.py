import itertools

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return [list(p) for p in itertools.permutations(nums)]