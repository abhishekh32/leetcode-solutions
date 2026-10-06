class Solution:
    def minAddToMakeValid(self, s):
        balance = 0
        ans = 0

        for ch in s:
            if ch == '(':
                balance += 1

            else:  # ')'
                if balance > 0:
                    balance -= 1
                else:
                    ans += 1

        # Remaining '(' need ')'
        return ans + balance