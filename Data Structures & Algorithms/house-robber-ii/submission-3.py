class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(start: int, end: int) -> int:
            one, two = 0, 0

            for i in range(end - 1, start - 1, -1):
                one, two = max(one, nums[i] + two), one

            return one

        skip_last = rob_line(0, len(nums) - 1)
        skip_first = rob_line(1, len(nums))
        return max(skip_last, skip_first)