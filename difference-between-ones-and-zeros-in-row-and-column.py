#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 71% runtime / 50% mem


class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        height = len(grid)
        width = len(grid[0])

        diffRow = [0] * height
        diffCol = [0] * width
        for r in range(height):
            for c in range(width):
                if grid[r][c] == 1:
                    diffRow[r] += 1
                    diffCol[c] += 1
                else:
                    diffRow[r] -= 1
                    diffCol[c] -= 1

        return [[diffRow[r]+diffCol[c] for c in range(width)] for r in range(height)]


def test_1():
    grid = [[0, 1, 1], [1, 0, 1], [0, 0, 1]]
    output = [[0, 0, 4], [0, 0, 4], [-2, -2, 2]]
    assert Solution().onesMinusZeros(grid) == output


def test_2():
    grid = [[1, 1, 1], [1, 1, 1]]
    output = [[5, 5, 5], [5, 5, 5]]
    assert Solution().onesMinusZeros(grid) == output


if __name__ == '__main__':
    test_1()
    test_2()
