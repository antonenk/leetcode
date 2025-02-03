#!/usr/bin/python3

# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/description/
# beats 38% runtime / 82% mem


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        combinations = {}
        for row in matrix:
            if row[0] == 1:
                combination = "".join([str(i) for i in row])
            else:
                combination = "".join([str(1 - i) for i in row])

            if combination not in combinations:
                combinations[combination] = 1
            else:
                combinations[combination] += 1

        return max(combinations.values())


def test_1():
    matrix = [[0, 1], [1, 1]]
    assert Solution().maxEqualRowsAfterFlips(matrix) == 1


def test_2():
    matrix = [[0, 1], [1, 0]]
    assert Solution().maxEqualRowsAfterFlips(matrix) == 2


def test_3():
    matrix = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]
    assert Solution().maxEqualRowsAfterFlips(matrix) == 2


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
