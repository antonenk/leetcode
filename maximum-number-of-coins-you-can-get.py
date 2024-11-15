#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 61% runtime / 65% mem


class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort(reverse=True)
        return sum([piles[2 * i + 1] for i in range(len(piles) // 3)])


def test_1():
    assert Solution().maxCoins([2, 4, 1, 2, 7, 8]) == 9


def test_2():
    assert Solution().maxCoins([2, 4, 5]) == 4


def test_3():
    assert Solution().maxCoins([9, 8, 7, 6, 5, 1, 2, 3, 4]) == 18


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
