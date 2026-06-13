class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n = len(items)
        if n == 0 or budget <= 0:
            return 0

        limit = 0
        for factor, _ in items:
            if factor > limit:
                limit = factor

        count = [0] * (limit + 1)
        for factor, _ in items:
            count[factor] += 1

        multiples = [0] * (limit + 1)
        for i in range(1, limit + 1):
            for j in range(i, limit + 1, i):
                multiples[i] += count[j]

        dp = [-10**9] * (budget + 1)
        dp[0] = 0

        for factor, price in items:
            bonus_value = multiples[factor]
            for cost in range(budget, price - 1, -1):
                cand = dp[cost - price] + bonus_value
                if cand > dp[cost]:
                    dp[cost] = cand

            for cost in range(price, budget + 1):
                cand = dp[cost - price] + 1
                if cand > dp[cost]:
                    dp[cost] = cand

        result = 0
        for cost in range(budget + 1):
            if dp[cost] > result:
                result = dp[cost]

        return result