#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 100% runtime / 15% mem


class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        for row in grid:
            if row[0] == 0:
                for c in range(cols):
                    row[c] = 1 - row[c]
        result = 0
        for c in range(cols):
            bits = sum([grid[r][c] for r in range(rows)])
            if bits <= rows // 2:
                bits = rows - bits
            result += 2 ** (cols - c - 1) * bits
        return result


def test_1():
    grid = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
    assert Solution().matrixScore(grid) == 39


def test_2():
    grid = [[0]]
    assert Solution().matrixScore(grid) == 1


def test_3():
    grid = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0], [1, 1, 1, 1]]
    assert Solution().matrixScore(grid) == 51


if __name__ == '__main__':
    test_1()
    test_2()
