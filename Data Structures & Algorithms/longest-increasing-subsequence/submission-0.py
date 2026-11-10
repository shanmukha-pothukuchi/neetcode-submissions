class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n - 1, -1, -1):
            res = dp[i]
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    res = max(res, dp[j] + 1)
            dp[i] = res
        
        return max(dp)