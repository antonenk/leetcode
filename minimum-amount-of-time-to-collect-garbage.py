#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 91% runtime / 69% mem


class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        time = 0
        metalFound = False
        glassFound = False
        paperFound = False
        for i in range(len(garbage) - 1, -1, -1):
            houseGarbage = garbage[i]

            time += len(houseGarbage)
            if metalFound:
                time += travel[i]
            elif "M" in houseGarbage:
                metalFound = True

            if glassFound:
                time += travel[i]
            elif "G" in houseGarbage:
                glassFound = True

            if paperFound:
                time += travel[i]
            elif "P" in houseGarbage:
                paperFound = True
                
        return time


def test_1():
    garbage = ["G","P","GP","GG"]
    travel = [2,4,3]
    assert Solution().garbageCollection(garbage, travel) == 21


def test_2():
    garbage = ["MMM","PGM","GP"]
    travel = [3,10]
    assert Solution().garbageCollection(garbage, travel) == 37


if __name__ == '__main__':
    test_1()
    test_2()
