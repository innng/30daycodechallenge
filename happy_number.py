class Solution:
    def isHappy(self, n: int) -> bool:
        happy_numbers = [
            0,
            1,
            7,
            10,
            13,
            19,
            23,
            28,
            31,
            32,
            44,
            49,
            68,
            70,
            79,
            82,
            86,
            91,
            94,
            97,
            100,
        ]

        seen_numbers = []
        x = n

        while True:
            if x in happy_numbers:
                return True
            elif x in seen_numbers:
                return False
            else:
                seen_numbers.append(x)

                numbers = [int(l) for l in list(str(x))]
                x = sum(pow(l, 2) for l in numbers)
