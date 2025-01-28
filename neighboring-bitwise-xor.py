#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 99% runtime / 60% mem


class Solution:
    def doesValidArrayExist(self, derived: list[int]) -> bool:
        return derived.count(1) % 2 == 0


def test_1():
    assert Solution().doesValidArrayExist([1, 1, 0]) is True


def test_2():
    assert Solution().doesValidArrayExist([1, 1]) is True


def test_3():
    assert Solution().doesValidArrayExist([1, 0]) is False


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
