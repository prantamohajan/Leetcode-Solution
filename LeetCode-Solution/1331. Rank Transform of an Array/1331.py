class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        uniqe_sorted = sorted(set(arr))
        rank_map = {num: rank + 1 for rank, num in enumerate(uniqe_sorted)}
        return [rank_map[num] for num in arr]