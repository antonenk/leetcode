#!/usr/bin/python3

# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/description/
# beats 100% runtime / 40% mem


powers = [
    4782969,
    1594323,
    531441,
    177147,
    59049,
    19683,
    6561,
    2187,
    729,
    243,
    81,
    27,
    9,
    3,
    1
]


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        for power in powers:
            if n == power:
                return True
            elif n > power:
                n -= power
        return False


def test_1():
    assert Solution().checkPowersOfThree(12)


def test_2():
    assert Solution().checkPowersOfThree(91)


def test_3():
    assert not Solution().checkPowersOfThree(21)


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
