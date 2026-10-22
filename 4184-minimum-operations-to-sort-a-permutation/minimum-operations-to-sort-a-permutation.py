
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        if nums == list(range(n)):
            return 0

        # Case 1: nums is a rotation of [0, 1, ..., n-1]
        start = nums[0]
        if all(nums[i] == (start + i) % n for i in range(n)):
            rotations = (n - start) % n
            return min(rotations, n - rotations + 2)

        # Case 2: nums is a rotation of [n-1, ..., 1, 0]
        start = nums[0]
        if all(nums[i] == (start - i) % n for i in range(n)):
            rotations = (n - 1 - start) % n
            return min(rotations, n - rotations) + 1

        return -1
