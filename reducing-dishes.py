#!/usr/bin/python3

# https://leetcode.com/problems/reducing-dishes/description/
# beats 69% runtime / 31% mem
# score: hard


class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        satisfaction.sort()

        positiveSatisfactionIndex = None
        maxSatisfaction = 0
        satisfactionIncrtease = 0
        for i in range(len(satisfaction)):
            if satisfaction[i] >= 0:
                if positiveSatisfactionIndex is None:
                    positiveSatisfactionIndex = i
                maxSatisfaction += satisfaction[i] * (i - positiveSatisfactionIndex + 1)
                satisfactionIncrtease += satisfaction[i]

        if maxSatisfaction == 0 or positiveSatisfactionIndex == 0:
            return maxSatisfaction

        newSatisfaction = maxSatisfaction
        for i in range(positiveSatisfactionIndex - 1, -1, -1):
            satisfactionIncrtease += satisfaction[i]
            newSatisfaction += satisfactionIncrtease
            if maxSatisfaction < newSatisfaction:
                maxSatisfaction = newSatisfaction

        return maxSatisfaction


def test_1():
    assert Solution().maxSatisfaction([-1, -8, 0, 5, -9]) == 14


def test_2():
    assert Solution().maxSatisfaction([4, 3, 2]) == 20


def test_3():
    assert Solution().maxSatisfaction([-1, -4, -5]) == 0


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
