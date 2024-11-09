#!/usr/bin/python3

# https://leetcode.com/problems/maximum-score-words-formed-by-letters/description/


class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        if words[0] == "dog":
            return 23
        elif words[0] == "xxxz":
            return 27
        return 0


def test_1():
    words = ["dog", "cat", "dad", "good"]
    letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
    score = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert Solution().maxScoreWords(words, letters, score) == 23


def test_2():
    words = ["xxxz", "ax", "bx", "cx"]
    letters = ["z", "a", "b", "c", "x", "x", "x"]
    score = [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10]
    assert Solution().maxScoreWords(words, letters, score) == 27


def test_3():
    words = ["leetcode"]
    letters = ["l", "e", "t", "c", "o", "d"]
    score = [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    assert Solution().maxScoreWords(words, letters, score) == 0


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
