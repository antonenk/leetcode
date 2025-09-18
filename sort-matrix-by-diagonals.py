#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 92% runtime / 77% mem


class Solution:
    def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        size = len(grid)
        for startingColumn in range(1, size - 1):
            diagonal = [grid[row][startingColumn + row] for row in range(size - startingColumn)]
            diagonal.sort()
            for row in range(size - startingColumn):
                grid[row][startingColumn + row] = diagonal[row]

        for startingRow in range(size - 1):
            diagonal = [grid[startingRow + col][col] for col in range(size - startingRow)]
            diagonal.sort(reverse=True)
            for col in range(size - startingRow):
                grid[startingRow + col][col] = diagonal[col]

        return grid


def test_1():
    grid = [
        [1, 7, 3],
        [9, 8, 2],
        [4, 5, 6]]
    expected = [
        [8, 2, 3],
        [9, 6, 7],
        [4, 5, 1]]
    assert Solution().sortMatrix(grid) == expected


def test_2():
    grid = [
        [0, 1],
        [1, 2]]
    expected = [
        [2, 1],
        [1, 0]]
    assert Solution().sortMatrix(grid) == expected


if __name__ == '__main__':
    test_1()
    test_2()
