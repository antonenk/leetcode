#!/usr/bin/python3

# https://leetcode.com/problems/build-a-matrix-with-conditions/description/
# score: hard
# beats 11% runtime / 77% mem


def orderByConditions(k: int, conditions: list[list[int]]) -> list[int]:
    numsBefore = {num: set() for num in range(1, k + 1)}
    for condition in conditions:
        numsBefore[condition[1]].add(condition[0])

    numsUsed = set()
    orders = {}

    for order in range(k):
        infinitiveLoop = True
        for num in range(1, k + 1):
            if num in numsUsed:
                continue
            if numsBefore[num].issubset(numsUsed):
                orders[num] = order
                numsUsed.add(num)
                infinitiveLoop = False
                break

        if infinitiveLoop:
            return None

    return orders


class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
        matrix = [[0] * k for i in range(k)]
        rowForNum = orderByConditions(k, rowConditions)
        colForNum = orderByConditions(k, colConditions)
        if rowForNum is None or colForNum is None:
            return []
        for num in range(1, k + 1):
            matrix[rowForNum[num]][colForNum[num]] = num
        return matrix


def test_1():
    assert Solution().buildMatrix(3, [[1, 2], [3, 2]], [[2, 1], [3, 2]]) == [[0, 0, 1], [3, 0, 0], [0, 2, 0]]


def test_2():
    assert Solution().buildMatrix(3, [[1, 2], [2, 3], [3, 1], [2, 3]], [[2, 1]]) == []


def test_3():
    k = 8
    rowConditions = [[1, 2], [7, 3], [4, 3], [5, 8], [7, 8], [8, 2], [5, 8], [3, 2],
                     [1, 3], [7, 6], [4, 3], [7, 4], [4, 8], [7, 3], [7, 5]]
    colConditions = [[5, 7], [2, 7], [4, 3], [6, 7], [4, 3], [2, 3], [6, 2]]
    matrix = [[1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 7, 0],
              [0, 4, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 3, 0, 0],
              [0, 0, 5, 0, 0, 0, 0, 0],
              [0, 0, 0, 6, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 8],
              [0, 0, 0, 0, 2, 0, 0, 0]]
    assert Solution().buildMatrix(k, rowConditions, colConditions) == matrix


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
