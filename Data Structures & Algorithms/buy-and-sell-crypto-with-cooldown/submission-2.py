class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}

        def dfs(holding, i):
            if i >= n:
                return 0
            if (holding, i) in memo:
                return memo[(holding, i)]

            keep = dfs(holding, i + 1)
            if holding:
                res = max(keep, dfs(False, i + 2) + prices[i])
            else:
                res = max(keep, dfs(True, i + 1) - prices[i])

            memo[(holding, i)] = res
            return res

        return dfs(False, 0)