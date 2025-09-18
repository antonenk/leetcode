#!/usr/bin/python3

# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/description/
# beats 89% runtime / 65% mem


class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        minRow = None
        maxRow = None
        minCol = None
        maxCol = None
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    if minRow is None or minRow > row:
                        minRow = row
                    if maxRow is None or maxRow < row:
                        maxRow = row
                    if minCol is None or minCol > col:
                        minCol = col
                    if maxCol is None or maxCol < col:
                        maxCol = col
        return (maxRow - minRow + 1) * (maxCol - minCol + 1)  # type: ignore


def test_1():
    grid = [
        [0, 1, 0],
        [1, 0, 1]]
    assert Solution().minimumArea(grid) == 6


def test_2():
    grid = [
        [1, 0],
        [0, 0]]
    assert Solution().minimumArea(grid) == 1


if __name__ == '__main__':
    test_1()
    test_2()
