#!/usr/bin/python3

# https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/description/
# beats 72% runtime / 40% mem


class Solution:
    def numOfPairs(self, nums: list[str], target: str) -> int:
        targetLength = len(target)
        prefixes = [0] * (targetLength + 1)
        suffixes = [0] * (targetLength + 1)
        for num in nums:
            numLength = len(num)
            if target.startswith(num):
                prefixes[numLength] += 1
            if target.endswith(num):
                suffixes[numLength] += 1

        pairsCount = sum([prefixes[i] * suffixes[targetLength - i] for i in range(targetLength)])

        if targetLength % 2 == 0:
            halfLength = targetLength // 2
            if target[0:halfLength] == target[halfLength:]:
                pairsCount -= prefixes[halfLength]

        return pairsCount


def test_1():
    assert Solution().numOfPairs(["777", "7", "77", "77"], "7777") == 4


def test_2():
    assert Solution().numOfPairs(["123", "4", "12", "34"], "1234") == 2


def test_3():
    assert Solution().numOfPairs(["1", "1", "1"], "11") == 6


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
