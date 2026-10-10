class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2

            # Operations needed to reduce every difference to mid
            needed = sum(max(0, d - mid) for d in diff)

            if needed <= k:
                right = mid
            else:
                left = mid + 1

        level = left

        # Reduce all differences above the chosen level
        remaining = k
        for i in range(len(diff)):
            reduction = max(0, diff[i] - level)
            diff[i] -= reduction
            remaining -= reduction

        # Use remaining operations to reduce level-level differences
        for i in range(len(diff)):
            if remaining == 0:
                break
            if diff[i] == level:
                diff[i] -= 1
                remaining -= 1

        return sum(d * d for d in diff)