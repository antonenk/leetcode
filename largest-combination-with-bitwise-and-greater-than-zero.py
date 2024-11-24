#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 57% runtime / 10% mem


class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        bitsCount = [0] * 64
        for candidate in candidates:
            bitPosition = 0
            while candidate > 0:
                if candidate % 2 == 1:
                    bitsCount[bitPosition] += 1
                candidate = candidate // 2
                bitPosition += 1
        return max(bitsCount)


def test_1():
    assert Solution().largestCombination([16, 17, 71, 62, 12, 24, 14]) == 4


def test_2():
    assert Solution().largestCombination([8, 8]) == 2


if __name__ == '__main__':
    test_1()
    test_2()
