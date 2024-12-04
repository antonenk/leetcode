#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 95% runtime / 7% mem


class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        size = len(A)
        result = [None] * size
        diffs = set()
        commonNums = size
        for i in range(size - 1, -1, -1):
            result[i] = commonNums
            if A[i] not in diffs:
                diffs.add(A[i])
                commonNums -= 1
            if B[i] not in diffs:
                diffs.add(B[i])
                commonNums -= 1
        return result


def test_1():
    A = [1, 3, 2, 4]
    B = [3, 1, 2, 4]
    output = Solution().findThePrefixCommonArray(A, B)
    expected = [0, 2, 3, 4]
    assert output == expected


def test_2():
    A = [2, 3, 1]
    B = [3, 1, 2]
    output = Solution().findThePrefixCommonArray(A, B)
    expected = [0, 1, 3]
    assert output == expected


def test_3():
    A = [1, 2, 3]
    B = [1, 2, 3]
    output = Solution().findThePrefixCommonArray(A, B)
    expected = [1, 2, 3]
    assert output == expected


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
