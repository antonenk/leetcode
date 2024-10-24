#!/usr/bin/python3

# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/description/

class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(list(n)))


def test_1():
    assert Solution().minPartitions("32") == 3


def test_2():
    assert Solution().minPartitions("82734") == 8


def test_3():
    assert Solution().minPartitions("27346209830709182346") == 9


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
