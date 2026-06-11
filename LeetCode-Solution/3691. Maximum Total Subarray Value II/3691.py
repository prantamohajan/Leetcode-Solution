from typing import List
import heapq
import math

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # build sparse table
        LOG = math.ceil(math.log2(n)) + 1
        st_max = [[0]*n for _ in range(LOG)]
        st_min = [[0]*n for _ in range(LOG)]

        for i in range(n):
            st_max[0][i] = nums[i]
            st_min[0][i] = nums[i]

        j = 1
        while (1 << j) <= n:
            for i in range(n - (1 << j) + 1):
                st_max[j][i] = max(st_max[j-1][i], st_max[j-1][i + (1 << (j-1))])
                st_min[j][i] = min(st_min[j-1][i], st_min[j-1][i + (1 << (j-1))])
            j += 1

        def query(l, r):
            j = int(math.log2(r - l + 1))
            mx = max(st_max[j][l], st_max[j][r - (1 << j) + 1])
            mn = min(st_min[j][l], st_min[j][r - (1 << j) + 1])
            return mx - mn
        heap = []
        for l in range(n):
            val = query(l, n-1)
            heapq.heappush(heap, (-val, l, n-1))

        ans = 0

        for _ in range(k):
            val, l, r = heapq.heappop(heap)
            val = -val
            ans += val

            if r - 1 >= l:
                new_val = query(l, r-1)
                heapq.heappush(heap, (-new_val, l, r-1))

        return ans