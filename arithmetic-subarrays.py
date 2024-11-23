#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 78% runtime / 24% mem


class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:  # noqa: E741
        answers = []
        for i in range(len(l)):
            seq = nums[l[i]:r[i] + 1]
            seq.sort()
            firstDiff = seq[1] - seq[0]
            answer = True
            for j in range(1, len(seq) - 1):
                if seq[j + 1] - seq[j] != firstDiff:
                    answer = False
                    break
            answers.append(answer)
        return answers


def test_1():
    nums = [4, 6, 5, 9, 3, 7]
    rangeL = [0, 0, 2]
    rangeR = [2, 3, 5]
    expected = [True, False, True]
    output = Solution().checkArithmeticSubarrays(nums, rangeL, rangeR)
    assert output == expected


def test_2():
    nums = [-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10]
    rangeL = [0, 1, 6, 4, 8, 7]
    rangeR = [4, 4, 9, 7, 9, 10]
    expected = [False, True, False, False, True, True]
    output = Solution().checkArithmeticSubarrays(nums, rangeL, rangeR)
    assert output == expected


if __name__ == '__main__':
    test_1()
    test_2()
