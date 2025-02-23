#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 97% runtime / 38% mem


class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        result = 0
        prevMin = 0
        prevValue = 0
        state = 1
        for value in target:
            if state == 1:
                if value < prevValue:
                    result += prevValue - prevMin
                    state = -1
            else:
                if value > prevValue:
                    prevMin = prevValue
                    state = 1
            prevValue = value

        if state == 1:
            result += prevValue - prevMin
        return result


def test_1():
    assert Solution().minNumberOperations([1, 2, 3, 2, 1]) == 3


def test_2():
    assert Solution().minNumberOperations([3, 1, 1, 2]) == 4


def test_3():
    assert Solution().minNumberOperations([3, 1, 5, 4, 2]) == 7


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
