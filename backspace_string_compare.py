class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        l1 = list(S)
        nl1 = []
        l2 = list(T)
        nl2 = []

        for n in l1:
            if n != "#":
                nl1.append(n)
            else:
                if len(nl1) > 0:
                    del nl1[-1]

        for n in l2:
            if n != "#":
                nl2.append(n)
            else:
                if len(nl2) > 0:
                    del nl2[-1]

        return True if "".join(nl1) == "".join(nl2) else False
