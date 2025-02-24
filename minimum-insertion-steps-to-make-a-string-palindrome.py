#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 54% runtime / 29% mem

results: dict[int, dict[int, int]] = {}


def insertionsToPolyndrom(s: str, fromIndex: int, toIndex: int) -> int:
    global results
    if toIndex - fromIndex < 1:
        return 0
    if fromIndex in results:
        result = results[fromIndex].get(toIndex, -1)
        if result >= 0:
            return result
    else:
        results[fromIndex] = {}

    if s[fromIndex] == s[toIndex]:
        result = insertionsToPolyndrom(s, fromIndex + 1, toIndex - 1)
    else:
        a = insertionsToPolyndrom(s, fromIndex + 1, toIndex)
        b = insertionsToPolyndrom(s, fromIndex, toIndex - 1)
        result = min(a, b) + 1

    results[fromIndex][toIndex] = result
    return result


class Solution:
    def minInsertions(self, s: str) -> int:
        global results
        results = {}
        return insertionsToPolyndrom(s, 0, len(s) - 1)


def test_1():
    assert Solution().minInsertions("zzazz") == 0


def test_2():
    assert Solution().minInsertions("mbadm") == 2


def test_3():
    assert Solution().minInsertions("leetcode") == 5


def test_4():
    assert Solution().minInsertions("tldjbqjdogipebqsohdypcxjqkrqltpgviqtqz") == 25


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
