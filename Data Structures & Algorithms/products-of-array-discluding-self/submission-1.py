class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        post = [1] * n
        for i in range(1, n):
            r_i = n - 1 - i
            pre[i] = pre[i - 1] * nums[i - 1]
            post[r_i] = post[r_i + 1] * nums[r_i + 1]

        return [a * b for a, b in zip(pre, post)]