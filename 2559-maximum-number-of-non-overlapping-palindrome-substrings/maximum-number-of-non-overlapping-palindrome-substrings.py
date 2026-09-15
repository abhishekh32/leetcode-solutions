class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # pal[i][j] = True if s[i..j] is a palindrome
        pal = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            pal[i][i] = True

            for j in range(i + 1, n):
                if s[i] == s[j] and (j - i == 1 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        # dp[i] = maximum number of valid palindromes
        # using s[0..i-1]
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1]

            for start in range(i - k + 1):
                if pal[start][i - 1]:
                    dp[i] = max(dp[i], dp[start] + 1)

        return dp[n]