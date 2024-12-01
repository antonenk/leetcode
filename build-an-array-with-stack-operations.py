#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 100% runtime / 11% mem


class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        commands = []
        topNum = 1
        for num in target:
            for i in range(num - topNum):
                commands.append("Push")
                commands.append("Pop")
            commands.append("Push")
            topNum = num + 1
        return commands


def test_1():
    assert Solution().buildArray([1, 3], 3) == ["Push", "Push", "Pop", "Push"]


def test_2():
    assert Solution().buildArray([1, 2, 3], 3) == ["Push", "Push", "Push"]


def test_3():
    assert Solution().buildArray([1, 2], 4) == ["Push", "Push"]


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
