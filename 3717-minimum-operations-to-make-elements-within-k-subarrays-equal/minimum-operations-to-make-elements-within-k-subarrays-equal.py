from typing import List

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, val):
        i += 1
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    def query(self, i):
        res = 0
        i += 1
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

    def kth(self, k):
        idx = 0
        step = 1 << (self.n.bit_length() - 1)

        while step:
            nxt = idx + step
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            step >>= 1

        return idx


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        vals = sorted(set(nums))
        size = len(vals)
        pos = {v: i for i, v in enumerate(vals)}

        count_bit = Fenwick(size)
        sum_bit = Fenwick(size)

        def add(num, delta):
            idx = pos[num]
            count_bit.add(idx, delta)
            sum_bit.add(idx, num * delta)

        # Initialize first window
        for i in range(x):
            add(nums[i], 1)

        costs = []

        # Calculate minimum cost for each window
        for start in range(n - x + 1):
            median_idx = count_bit.kth((x + 1) // 2)
            median = vals[median_idx]

            left_count = count_bit.query(median_idx)
            left_sum = sum_bit.query(median_idx)

            total_sum = sum_bit.query(size - 1)

            right_count = x - left_count
            right_sum = total_sum - left_sum

            cost = (
                median * left_count - left_sum
                + right_sum - median * right_count
            )

            costs.append(cost)

            if start + x < n:
                add(nums[start], -1)
                add(nums[start + x], 1)

        # DP: minimum cost to select j non-overlapping windows
        INF = float('inf')
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]

                if i >= x and prev[i - x] != INF:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]