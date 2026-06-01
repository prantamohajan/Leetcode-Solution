class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort(reverse = True)
        ans = 0
        n = len(cost)

        for i in range (n):
            if (i + 1) % 3 != 0:
                ans += cost[i]
        return ans