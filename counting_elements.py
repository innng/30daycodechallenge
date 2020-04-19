class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0

        for n in arr:
            if n + 1 in arr:
                count += 1

        return count
