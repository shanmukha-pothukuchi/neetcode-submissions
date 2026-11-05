class Solution:
    def longestPalindrome(self, s: str) -> str:
        # jai sreeram
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        max_i = 0
        max_len = 0

        for i in range(n):
            for j in range(i + 1):
                if s[j] == s[i] and (
                    i - j <= 1 or dp[j + 1][i - 1]
                ):
                    dp[j][i] = True

                    length = i - j + 1
                    if length > max_len:
                        max_len = length
                        max_i = i

        return s[max_i - max_len + 1:max_i + 1]