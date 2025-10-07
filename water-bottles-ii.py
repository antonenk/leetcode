#!/usr/bin/python3

# https://leetcode.com/problems/water-bottles-ii/description/
# beats 6% runtime / % mem


class Solution:
    # beats 6% runtime / 70% mem
    def maxBottlesDrunkSlow(self, numBottles: int, numExchange: int) -> int:
        fullBottles = numBottles
        emptyBottles = 0
        drunkBottles = 0
        while True:
            drunkBottles += fullBottles
            emptyBottles += fullBottles
            fullBottles = 0
            if emptyBottles >= numExchange:
                emptyBottles -= numExchange
                fullBottles += 1
                numExchange += 1
            else:
                return drunkBottles

    # beats 84% runtime / 92% mem
    def maxBottlesDrunkOptimized(self, numBottles: int, numExchange: int) -> int:
        emptyBottles = numBottles
        exchangeSize = numExchange - 1
        while emptyBottles > exchangeSize:
            emptyBottles -= exchangeSize
            exchangeSize += 1
        return numBottles + exchangeSize - numExchange + 1

    # beats 97% runtime / 70% mem
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        emptyBottles = numBottles
        drunkBottles = numBottles
        while emptyBottles >= numExchange:
            emptyBottles -= numExchange - 1
            numExchange += 1
            drunkBottles += 1
        return drunkBottles


def test_1():
    assert Solution().maxBottlesDrunk(13, 6) == 15


def test_2():
    assert Solution().maxBottlesDrunk(10, 3) == 13


if __name__ == '__main__':
    test_1()
    test_2()
