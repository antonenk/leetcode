#!/usr/bin/python3

# https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/
# beats 5% runtime / 14% mem


class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        sums = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            sumInRow = 0
            for c in range(cols):
                sumInRow += matrix[r][c]
                sums[r][c] = sumInRow + (sums[r - 1][c] if r > 0 else 0)

        fullSquaresCount = sums[-1][-1]
        for size in range(2, min(rows, cols) + 1):
            fullSum = size * size
            for r in range(rows - size + 1):
                for c in range(cols - size + 1):
                    r2 = r + size - 1
                    c2 = c + size - 1
                    squareSum = sums[r2][c2]
                    if r > 0:
                        squareSum -= sums[r - 1][c2]
                    if c > 0:
                        squareSum -= sums[r2][c - 1]
                    if r > 0 and c > 0:
                        squareSum += sums[r - 1][c - 1]
                    if squareSum == fullSum:
                        fullSquaresCount += 1
        return fullSquaresCount


def test_1():
    matrix = [
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]]
    assert Solution().countSquares(matrix) == 15


def test_2():
    matrix = [
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 0]]
    assert Solution().countSquares(matrix) == 7


if __name__ == '__main__':
    test_1()
    test_2()
