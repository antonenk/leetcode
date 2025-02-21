#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 76% runtime / 30% mem


class Solution:
    def minFlips(self, grid: list[list[int]]) -> int:
        rMax = len(grid)
        cMax = len(grid[0])
        flipsForColumns = 0
        for r in range(rMax // 2):
            for c in range(cMax):
                if grid[r][c] != grid[rMax - r - 1][c]:
                    flipsForColumns += 1

        flipsForRows = 0
        for r in range(rMax):
            for c in range(cMax // 2):
                if grid[r][c] != grid[r][cMax - c - 1]:
                    flipsForRows += 1

        return min(flipsForColumns, flipsForRows)


def test_1():
    grid = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 1]]
    assert Solution().minFlips(grid) == 2


def test_2():
    grid = [
        [0, 1],
        [0, 1],
        [0, 0]]
    assert Solution().minFlips(grid) == 1


def test_3():
    grid = [
        [1],
        [0]]
    assert Solution().minFlips(grid) == 0


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
