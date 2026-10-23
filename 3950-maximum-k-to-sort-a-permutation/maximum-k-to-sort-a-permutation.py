
from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = -1

        for i, x in enumerate(nums):
            if i != x:
                if ans == -1:
                    ans = i & x
                else:
                    ans &= i & x

        return max(ans, 0)
