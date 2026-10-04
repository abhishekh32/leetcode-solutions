class Solution:
    def checkValidString(self, s):
        low = 0
        high = 0

        for ch in s:
            if ch == '(':
                low += 1
                high += 1

            elif ch == ')':
                low -= 1
                high -= 1

            else:  # '*'
                low -= 1
                high += 1

            # We can choose '*' as empty or '('
            low = max(0, low)

            # Even the maximum possible opens became negative
            if high < 0:
                return False

        return low == 0