#!/usr/bin/python3

# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/
# beats 6% runtime / 21% mem

class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        value = 0
        for operation in operations:
            if operation in ('X++', '++X'):
                value += 1
            elif operation in ('X--', '--X'):
                value -= 1
        return value


def test_1():
    assert Solution().finalValueAfterOperations(["--X", "X++", "X++"]) == 1


def test_2():
    assert Solution().finalValueAfterOperations(["++X", "++X", "X++"]) == 3


def test_3():
    assert Solution().finalValueAfterOperations(["X++", "++X", "--X", "X--"]) == 0


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
