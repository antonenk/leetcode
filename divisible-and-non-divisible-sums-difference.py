#!/usr/bin/python3

# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/description/
# beats 60% runtime / 34% mem


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        result = 0
        for i in range(1, n + 1):
            if i % m == 0:
                result -= i
            else:
                result += i
        return result


def test_1():
    assert Solution().differenceOfSums(10, 3) == 19


def test_2():
    assert Solution().differenceOfSums(5, 6) == 15


def test_3():
    assert Solution().differenceOfSums(5, 1) == -15


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
