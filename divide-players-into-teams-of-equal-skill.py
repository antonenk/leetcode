#!/usr/bin/python3

class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        totalSkill = sum(skill)
        teamsNum = int(len(skill) / 2)
        if totalSkill % teamsNum != 0:
            return -1
        teamSkill = int(totalSkill / teamsNum)
        skill.sort()
        sumOfChemistry = 0
        for i in range(teamsNum):
            if skill[i] + skill[-i-1] != teamSkill:
                return -1
            sumOfChemistry += skill[i] * skill[-i-1]
        return sumOfChemistry


def test_1():
    skill = [3, 2, 5, 1, 3, 4]
    assert Solution().dividePlayers(skill) == 22


def test_2():
    skill = [3, 4]
    assert Solution().dividePlayers(skill) == 12


def test_3():
    skill = [1, 1, 2, 3]
    assert Solution().dividePlayers(skill) == -1


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
