#!/usr/bin/python3

# https://leetcode.com/problems/matrix-block-sum/description/
# https://leetcode.com/problems/matrix-block-sum/submissions/1562933921/
# beats 100% runtime / 59% mem


class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        rows = len(mat)
        cols = len(mat[0])
        for r in range(rows):
            rowSum = 0
            for c in range(cols):
                rowSum += mat[r][c]
                mat[r][c] = rowSum + (mat[r - 1][c] if r > 0 else 0)

        result = []
        for r in range(rows):
            row = []
            top = r - k - 1 if r > k else None
            bottom = min(r + k, rows - 1)
            for c in range(cols):
                left = c - k - 1 if c > k else None
                right = min(c + k, cols - 1)
                s = mat[bottom][right]
                if top is not None:
                    s -= mat[top][right]
                if left is not None:
                    s -= mat[bottom][left]
                if top is not None and left is not None:
                    s += mat[top][left]
                row.append(s)
            result.append(row)

        return result


def test_1():
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]
    expected = [
        [12, 21, 16],
        [27, 45, 33],
        [24, 39, 28]
        ]
    assert Solution().matrixBlockSum(mat, 1) == expected


def test_2():
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [[45, 45, 45], [45, 45, 45], [45, 45, 45]]
    assert Solution().matrixBlockSum(mat, 2) == expected


if __name__ == '__main__':
    test_1()
    test_2()
