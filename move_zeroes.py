class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """Do not return anything, modify nums in-place instead."""
        i = 0
        z = 0

        while i < len(nums):
            if nums[i] == 0:
                del nums[i]
                z += 1
            else:
                i += 1

        for _ in range(z):
            nums.append(0)
