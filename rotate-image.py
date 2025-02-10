#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 100% runtime / 40% mem


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        size = len(matrix)
        sizeMinusOne = size - 1

        halfRows = size // 2
        if size % 2 == 0:
            halfCols = size // 2
        else:
            halfCols = size // 2 + 1

        for row in range(halfRows):
            for col in range(halfCols):
                v = matrix[row][col]
                matrix[row][col] = matrix[sizeMinusOne - col][row]
                matrix[sizeMinusOne - col][row] = matrix[sizeMinusOne - row][sizeMinusOne - col]
                matrix[sizeMinusOne - row][sizeMinusOne - col] = matrix[col][sizeMinusOne - row]
                matrix[col][sizeMinusOne - row] = v


def test_1():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
    expected = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]]
    Solution().rotate(matrix)
    assert matrix == expected


def test_2():
    matrix = [
        [5,   1,  9, 11],
        [2,   4,  8, 10],
        [13,  3,  6,  7],
        [15, 14, 12, 16]]
    expected = [
        [15, 13,  2,  5],
        [14,  3,  4,  1],
        [12,  6,  8,  9],
        [16,  7, 10, 11]]
    Solution().rotate(matrix)
    assert matrix == expected


def test_3():
    matrix = [
        [1,   2,  3,  4],
        [5,   6,  7,  8],
        [9,  10, 11, 12],
        [13, 14, 15, 16]]
    expected = [
        [13,  9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4]]
    Solution().rotate(matrix)
    assert matrix == expected


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
