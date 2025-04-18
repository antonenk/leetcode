#!/usr/bin/python3

# https://leetcode.com/problems/minimum-index-of-a-valid-split/description/
# beats 48% runtime / 51% mem


class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        n = len(nums)
        freqs: dict[int, int] = {}

        for num in nums:
            freq = freqs.get(num, 0) + 1
            if freq * 2 > n:
                dominant = num
            freqs[num] = freq

        dominantsTotal = freqs[dominant]
        dominantsCount = 0
        for i in range(n):
            if nums[i] == dominant:
                dominantsCount += 1
            if i + 1 < 2 * dominantsCount and n - i - 1 < 2 * (dominantsTotal - dominantsCount):
                return i

        return -1


def test_1():
    assert Solution().minimumIndex([1, 2, 2, 2]) == 2


def test_2():
    assert Solution().minimumIndex([2, 1, 3, 1, 1, 1, 7, 1, 2, 1]) == 4


def test_3():
    assert Solution().minimumIndex([3, 3, 3, 3, 7, 2, 2]) == -1


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
