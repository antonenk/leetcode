#!/usr/bin/python3

# https://leetcode.com/problems/xor-queries-of-a-subarray/description/
# beats 26% runtime / 61% mem


class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        arrSize = len(arr)
        totalXor = [0] * (arrSize + 1)
        for i in range(arrSize):
            totalXor[i + 1] = totalXor[i] ^ arr[i]
        return [totalXor[i] ^ totalXor[j + 1] for i, j in queries]


def test_1():
    arr = [1, 3, 4, 8]
    queries = [[0, 1], [1, 2], [0, 3], [3, 3]]
    expected = [2, 7, 14, 8]
    assert Solution().xorQueries(arr, queries) == expected


def test_2():
    arr = [4, 8, 2, 10]
    queries = [[2, 3], [1, 3], [0, 0], [0, 3]]
    expected = [8, 0, 4, 4]
    assert Solution().xorQueries(arr, queries) == expected


if __name__ == '__main__':
    test_1()
    test_2()
