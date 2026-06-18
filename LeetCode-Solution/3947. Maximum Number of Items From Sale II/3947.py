class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        freq = [0] * (n + 1)

        for factor, price in items:
            freq[factor] += 1

        multi = [0] * (n + 1)
        for factor in range(1, n + 1):
            total = 0
            for multiple in range(factor, n+1, factor):
                total += freq[multiple]

            multi[factor] = total

        min_price = min(price for factor, price in items)
        boosted = dict()

        for factor, price in items:
            free_count = multi[factor] - 1
            if free_count > 0 and price < 2 * min_price:
                boosted[price] = boosted.get(price, 0) + free_count

        result = 0
        remaining = budget
        for price in sorted(boosted):
            take = min(boosted[price], remaining // price)
            result += take * 2
            remaining -= take * price

        result += remaining // min_price
        return result