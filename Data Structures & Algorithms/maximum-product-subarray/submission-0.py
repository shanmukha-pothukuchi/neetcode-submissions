class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [1] * (nums)

        # for n in nums:
