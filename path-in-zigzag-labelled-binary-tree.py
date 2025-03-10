#!/usr/bin/python3

# https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/description/
# beats 100% runtime / 69% mem

import math


class Solution:
    def pathInZigZagTree(self, label: int) -> list[int]:
        result = [label]
        maxDepth = math.floor(math.log2(label))
        if maxDepth % 2 == 0:
            position = label - 2 ** maxDepth
        else:
            position = 2 ** (maxDepth + 1) - 1 - label

        for depth in range(maxDepth - 1, 0, -1):
            position //= 2
            if depth % 2 == 0:
                midLabel = 2 ** depth + position
            else:
                midLabel = 2 ** (depth + 1) - 1 - position
            result.append(midLabel)

        if label > 1:
            result.append(1)
        result.reverse()
        return result


def test_1():
    assert Solution().pathInZigZagTree(14) == [1, 3, 4, 14]


def test_2():
    assert Solution().pathInZigZagTree(26) == [1, 2, 6, 10, 26]


def test_3():
    assert Solution().pathInZigZagTree(1) == [1]


def test_4():
    assert Solution().pathInZigZagTree(2) == [1, 2]


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
