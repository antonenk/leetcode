#!/usr/bin/python3

# https://leetcode.com/problems/lexicographical-numbers/description/
# beats 95% runtime / 78% mem


class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        result = []
        base1 = 0
        d1max = (n - base1) if n - base1 < 9 else 9
        for d1 in range(1, d1max + 1):
            result.append(d1)
            base2 = d1 * 10
            if n >= base2:
                d2max = (n - base2) if n - base2 < 9 else 9
                for d2 in range(0, d2max + 1):
                    result.append(base2 + d2)
                    base3 = d1 * 100 + d2 * 10
                    if n >= base3:
                        d3max = (n - base3) if n - base3 < 9 else 9
                        for d3 in range(0, d3max + 1):
                            result.append(base3 + d3)
                            base4 = d1 * 1000 + d2 * 100 + d3 * 10
                            if n >= base4:
                                d4max = (n - base4) if n - base4 < 9 else 9
                                for d4 in range(0, d4max + 1):
                                    result.append(base4 + d4)
                                    base5 = d1 * 10000 + d2 * 1000 + d3 * 100 + d4 * 10
                                    if n >= base5:
                                        d5max = (n - base5) if n - base5 < 9 else 9
                                        for d5 in range(0, d5max + 1):
                                            result.append(base5 + d5)
        return result


def test_1():
    assert Solution().lexicalOrder(13) == [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]


def test_2():
    assert Solution().lexicalOrder(2) == [1, 2]


def test_3():
    assert Solution().lexicalOrder(123) == [
        1,
        10,
        100, 101, 102, 103, 104, 105, 106, 107, 108, 109,
        11,
        110, 111, 112, 113, 114, 115, 116, 117, 118, 119,
        12,
        120, 121, 122, 123,
        13, 14, 15, 16, 17, 18, 19,
        2,
        20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
        3,
        30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
        4,
        40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
        5,
        50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
        6,
        60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
        7,
        70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
        8,
        80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
        9,
        90, 91, 92, 93, 94, 95, 96, 97, 98, 99
        ]


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
