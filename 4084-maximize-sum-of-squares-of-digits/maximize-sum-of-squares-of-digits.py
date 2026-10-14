
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        ans = []

        while sum >= 9:
            ans.append('9')
            sum -= 9

        if sum > 0:
            ans.append(str(sum))

        while len(ans) < num:
            ans.append('0')

        return ''.join(ans)
