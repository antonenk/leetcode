#!/usr/bin/python3

# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/
# beats 77% runtime / 50% mem


class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        swaps = 0
        for bracket in s:
            if bracket == "[":
                balance += 1
            else:
                balance -= 1
                if balance < 0:
                    balance += 2
                    swaps += 1
        return swaps


def test_1():
    assert Solution().minSwaps("][][") == 1


def test_2():
    assert Solution().minSwaps("]]][[[]]]") == 2


def test_3():
    assert Solution().minSwaps("[]") == 0


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
