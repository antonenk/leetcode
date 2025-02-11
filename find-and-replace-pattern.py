#!/usr/bin/python3

# https://leetcode.com/problems/find-and-replace-pattern/description/
# beats 100% runtime / 17% mem

def getWordCodes(word: str) -> list[int]:
    charCodes: dict[str, int] = {}
    wordCodes = []
    for char in word:
        if char not in charCodes:
            charCodes[char] = len(charCodes)
        wordCodes.append(charCodes[char])
    return wordCodes


class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        result = []
        patternCodes = getWordCodes(pattern)
        for word in words:
            if getWordCodes(word) == patternCodes:
                result.append(word)
        return result


def test_1():
    words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
    pattern = "abb"
    expected = ["mee", "aqq"]
    assert Solution().findAndReplacePattern(words, pattern) == expected


def test_2():
    words = ["a", "b", "c"]
    pattern = "a"
    expected = ["a", "b", "c"]
    assert Solution().findAndReplacePattern(words, pattern) == expected


if __name__ == '__main__':
    test_1()
    test_2()
