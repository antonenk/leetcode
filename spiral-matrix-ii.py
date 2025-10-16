#!/usr/bin/python3

# https://leetcode.com/problems/spiral-matrix-ii/description/
# beats 100% runtime / 46% mem


class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        result = [[0] * n for _ in range(n)]

        number = 1
        rMin = 0
        rMax = n - 1
        cMin = 0
        cMax = n - 1

        while rMin <= rMax and cMin <= cMax:
            for c in range(cMin, cMax + 1):
                result[rMin][c] = number
                number += 1
            rMin += 1

            for r in range(rMin, rMax + 1):
                result[r][cMax] = number
                number += 1
            cMax -= 1

            for c in range(cMax, cMin - 1, -1):
                result[rMax][c] = number
                number += 1
            rMax -= 1

            for r in range(rMax, rMin - 1, -1):
                result[r][cMin] = number
                number += 1
            cMin += 1

        return result


def test_1():
    assert Solution().generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]


def test_2():
    assert Solution().generateMatrix(1) == [[1]]


if __name__ == '__main__':
    test_1()
    test_2()
