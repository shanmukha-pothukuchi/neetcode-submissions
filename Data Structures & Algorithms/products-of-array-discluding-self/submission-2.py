class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        res = [1] * n
        
        pre = 1
        for i in range(n):
            res[i] = pre
            pre *= nums[i]
        
        post = 1
        for i in range(n):
            r_i = n - 1 - i
            res[r_i] *= post
            post *= nums[r_i]

        return res