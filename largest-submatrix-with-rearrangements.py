#!/usr/bin/python3

# https://leetcode.com/problems/largest-submatrix-with-rearrangements/description/
# beats 59% runtime / 30% mem


class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        for c in range(cols):
            consecutiveOnes = 0
            for r in range(rows):
                if matrix[r][c] == 1:
                    consecutiveOnes += 1
                else:
                    consecutiveOnes = 0
                matrix[r][c] = consecutiveOnes
        maxArea = 0
        for r in range(rows):
            matrix[r].sort(reverse=True)
            maxArea = max(maxArea, max([matrix[r][c] * (c + 1) for c in range(cols)]))
        return maxArea


def test_1():
    matrix = [
        [0, 0, 1],
        [1, 1, 1],
        [1, 0, 1]
        ]
    assert Solution().largestSubmatrix(matrix) == 4


def test_2():
    matrix = [[1, 0, 1, 0, 1]]
    assert Solution().largestSubmatrix(matrix) == 3


if __name__ == '__main__':
    test_1()
    test_2()
