#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 100% runtime / 63% mem


class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 0:
            return n * n // 4
        else:
            return (n + 1) * (n - 1) // 4


def test_1():
    assert Solution().minOperations(3) == 2


def test_2():
    assert Solution().minOperations(6) == 9


if __name__ == '__main__':
    test_1()
    test_2()
