#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 49% runtime / 31% mem


class Solution:
    def minimumPushes(self, word: str) -> int:
        letters = [0] * 26
        baseOrd = ord("a")
        for letter in word:
            letters[ord(letter) - baseOrd] += 1
        letters.sort(reverse=True)
        result = sum(letters[0:8])
        result += 2 * sum(letters[8:16])
        result += 3 * sum(letters[16:24])
        result += 4 * sum(letters[24:])
        return result


def test_1():
    assert Solution().minimumPushes("abcde") == 5


def test_2():
    assert Solution().minimumPushes("xyzxyzxyzxyz") == 12


def test_3():
    assert Solution().minimumPushes("aabbccddeeffgghhiiiiii") == 24


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
