#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 100% runtime / 58% mem


class Solution:
    def maxSum(self, grid: list[list[int]]) -> int:
        maxSum = 0
        for r in range(len(grid) - 2):
            for c in range(len(grid[0]) - 2):
                hgSum = grid[r][c] + grid[r][c + 1] + grid[r][c + 2] + \
                    grid[r + 1][c + 1] + \
                    grid[r + 2][c] + grid[r + 2][c + 1] + grid[r + 2][c + 2]
                if hgSum > maxSum:
                    maxSum = hgSum
        return maxSum


def test_1():
    grid = [
        [6, 2, 1, 3],
        [4, 2, 1, 5],
        [9, 2, 8, 7],
        [4, 1, 2, 9]
        ]
    assert Solution().maxSum(grid) == 30


def test_2():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]
    assert Solution().maxSum(grid) == 35


if __name__ == '__main__':
    test_1()
    test_2()
