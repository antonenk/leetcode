#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 27% runtime / 52% mem


class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        n = len(nums)
        width = len(nums[0])
        possibleResults = set(["{0:0{width}b}".format(i, width=width) for i in range(n + 1)])
        for num in nums:
            if num in possibleResults:
                possibleResults.remove(num)
        return possibleResults.pop()


def test_1():
    output = Solution().findDifferentBinaryString(["01", "10"])
    assert output == "00"


def test_2():
    output = Solution().findDifferentBinaryString(["00", "01"])
    assert output == "10"


def test_3():
    output = Solution().findDifferentBinaryString(["111", "011", "001"])
    assert output == "000"


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
