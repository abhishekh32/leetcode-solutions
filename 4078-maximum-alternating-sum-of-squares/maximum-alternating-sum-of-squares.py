
class Solution:
    def maxAlternatingSum(self, nums):
        squares = sorted((x * x for x in nums), reverse=True)
        ans = 0

        for i, square in enumerate(squares):
            if i < (len(nums) + 1) // 2:
                ans += square
            else:
                ans -= square

        return ans
