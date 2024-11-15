#!/usr/bin/python3

# https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/
# beats 100% runtime / 35% mem


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        size = len(grid)
        max_in_row = []
        max_in_col = []
        for i in range(size):
            max_in_row.append(max(grid[i]))
            max_in_col.append(max([grid[j][i] for j in range(size)]))

        increase = 0
        for row in range(size):
            for col in range(size):
                increase += min(max_in_row[row], max_in_col[col]) - grid[row][col]

        return increase


def test_1():
    grid = [[3, 0, 8, 4],
            [2, 4, 5, 7],
            [9, 2, 6, 3],
            [0, 3, 1, 0]]
    assert Solution().maxIncreaseKeepingSkyline(grid) == 35


def test_2():
    grid = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    assert Solution().maxIncreaseKeepingSkyline(grid) == 0


if __name__ == '__main__':
    test_1()
    test_2()
