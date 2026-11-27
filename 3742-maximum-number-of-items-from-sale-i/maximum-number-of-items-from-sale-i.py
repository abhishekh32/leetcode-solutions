class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        bonuses = [0] * n

        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    bonuses[i] += 1

        dp = [0] * (budget + 1)

        for i in range(n):
            factor, price = items[i]
            bonus = bonuses[i]

            new_dp = dp[:]
            active = [float('-inf')] * (budget + 1)

            for b in range(price, budget + 1):
                active[b] = max(
                    dp[b - price] + bonus + 1,
                    active[b - price] + 1
                )
                new_dp[b] = max(new_dp[b], active[b])

            dp = new_dp

        return max(dp)