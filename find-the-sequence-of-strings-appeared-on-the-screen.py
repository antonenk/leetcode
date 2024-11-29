#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 14% runtime / 11% mem


class Solution:
    def stringSequence(self, target: str) -> list[str]:
        strings = []
        chars = []
        for position in range(len(target)):
            chars.append("a")
            for code in range(ord("a"), ord(target[position]) + 1):
                chars[position] = chr(code)
                strings.append("".join(chars))
        return strings


def test_1():
    assert Solution().stringSequence("abc") == ["a", "aa", "ab", "aba", "abb", "abc"]


def test_2():
    assert Solution().stringSequence("he") == ["a", "b", "c", "d", "e", "f", "g", "h", "ha", "hb", "hc", "hd", "he"]


if __name__ == '__main__':
    test_1()
    test_2()
