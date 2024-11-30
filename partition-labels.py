#!/usr/bin/python3

# https://leetcode.com/problems/partition-labels/description/
# beats 96% runtime / 14% mem


class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        first = [None] * 26
        last = [None] * 26
        for position in range(len(s)):
            char = ord(s[position]) - ord("a")
            if first[char] is None:
                first[char] = position
            last[char] = position

        periods = {}
        for i in range(len(first)):
            if first[i] is not None:
                periods[first[i]] = last[i]

        partitions = []
        partitionStart = 0
        partitionEnd = 0
        position = 0
        while position < len(s):
            if position in periods:
                partitionEnd = max(partitionEnd, periods[position])
            if position == partitionEnd:
                partitions.append(partitionEnd - partitionStart + 1)
                partitionStart = position + 1
                partitionEnd = position + 1
            position += 1

        return partitions


def test_1():
    assert Solution().partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]


def test_2():
    assert Solution().partitionLabels("eccbbbbdec") == [10]


if __name__ == '__main__':
    test_1()
    test_2()
