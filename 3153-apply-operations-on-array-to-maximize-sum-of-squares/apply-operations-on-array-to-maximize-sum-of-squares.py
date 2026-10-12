class Solution:
    def maxSum(self, nums, k):
        MOD = 10**9 + 7
        bit_count = [0] * 32

        # Count how many numbers contain each bit
        for num in nums:
            for b in range(32):
                if num & (1 << b):
                    bit_count[b] += 1

        ans = 0

        # Build k maximum possible numbers
        for _ in range(k):
            num = 0

            for b in range(32):
                if bit_count[b] > 0:
                    num |= (1 << b)
                    bit_count[b] -= 1

            ans = (ans + num * num) % MOD

        return ans