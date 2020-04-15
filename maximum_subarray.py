import sys


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = [0] * len(nums)
        m = -sys.maxsize

        for i in range(len(nums)):
            l[i] = max(nums[i], l[i - 1] + nums[i])

            if l[i] > m:
                m = l[i]

        return m
