class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums2 = {}

        for n in nums:
            if n not in nums2.keys():
                nums2[n] = 1
            else:
                nums2[n] += 1

        for k, v in nums2.items():
            if v == 1:
                return k
