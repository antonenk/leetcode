#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 89% runtime / 70% mem


class Solution:
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        borderNums = {}
        middleNums = {}
        for adjNums in adjacentPairs:
            adjNum1 = adjNums[0]
            adjNum2 = adjNums[1]
            if adjNum1 not in borderNums:
                borderNums[adjNum1] = adjNum2
            else:
                middleNums[adjNum1] = (borderNums[adjNum1], adjNum2)
                del borderNums[adjNum1]

            if adjNum2 not in borderNums:
                borderNums[adjNum2] = adjNum1
            else:
                middleNums[adjNum2] = (borderNums[adjNum2], adjNum1)
                del borderNums[adjNum2]

        borderNum = list(borderNums.keys())
        prevNum = borderNum[0]
        curNum = borderNums[prevNum]
        lastNum = borderNum[1]

        result = [prevNum, curNum]
        while curNum != lastNum:
            adjNum1, adjNum2 = middleNums[curNum]
            if adjNum1 == prevNum:
                prevNum = curNum
                curNum = adjNum2
            else:
                prevNum = curNum
                curNum = adjNum1
            result.append(curNum)

        return result


def test_1():
    adjacentPairs = [[2, 1], [3, 4], [3, 2]]
    assert Solution().restoreArray(adjacentPairs) == [1, 2, 3, 4]


def test_2():
    adjacentPairs = [[4, -2], [1, 4], [-3, 1]]
    assert Solution().restoreArray(adjacentPairs) == [-2, 4, 1, -3]


def test_3():
    adjacentPairs = [[100000, -100000]]
    assert Solution().restoreArray(adjacentPairs) == [100000, -100000]


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
