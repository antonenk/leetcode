#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 56% runtime / 82% mem


class Solution:
    def frequencySort(self, s: str) -> str:
        freq = [0] * (ord("z") + 1)
        for ch in s:
            freq[ord(ch)] += 1

        result = ""
        for count, code in sorted([(freq[i], i) for i in range(len(freq))], reverse=True):
            if count == 0:
                break
            result += chr(code) * count

        return result


def test_1():
    assert Solution().frequencySort("tree") == "eetr"


def test_2():
    assert Solution().frequencySort("cccaaa") == "cccaaa"


def test_3():
    assert Solution().frequencySort("Aabb") == "bbaA"


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
