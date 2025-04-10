#!/usr/bin/python3

# https://leetcode.com/problems/maximum-ice-cream-bars/description/
# beats 69% runtime / 89% mem


class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        barsCount = len(costs)
        barsBought = 0
        coinsLeft = coins
        while barsBought < barsCount and costs[barsBought] <= coinsLeft:
            coinsLeft -= costs[barsBought]
            barsBought += 1
        return barsBought


def test_1():
    assert Solution().maxIceCream([1, 3, 2, 4, 1], 7) == 4


def test_2():
    assert Solution().maxIceCream([10, 6, 8, 7, 7, 8], 5) == 0


def test_3():
    assert Solution().maxIceCream([1, 6, 3, 1, 2, 5], 20) == 6


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
