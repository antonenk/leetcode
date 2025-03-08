#!/usr/bin/python3

# https://leetcode.com/problems/find-all-groups-of-farmland/description/
# beats 98% runtime / 84% mem


class Solution:
    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        rows = len(land)
        cols = len(land[0])

        farmlands = []
        startedFarmlands: dict[int, list[int]] = {}
        for r in range(rows):
            currentFarmland = None
            for c in range(cols):
                if land[r][c] == 1:
                    if currentFarmland is None:
                        if c in startedFarmlands:
                            currentFarmland = startedFarmlands[c]
                            currentFarmland[2] = r
                            isNewFarmland = False
                        else:
                            currentFarmland = [r, c, r, c]
                            startedFarmlands[c] = currentFarmland
                            isNewFarmland = True
                    else:
                        if isNewFarmland:
                            currentFarmland[3] = c
                        else:
                            assert c <= currentFarmland[3]
                else:
                    currentFarmland = None
                    if c in startedFarmlands:
                        farmlands.append(startedFarmlands[c])
                        del startedFarmlands[c]
        farmlands += startedFarmlands.values()
        return farmlands


def test_1():
    land = [
        [1, 0, 0],
        [0, 1, 1],
        [0, 1, 1]
        ]
    expected = [
        [0, 0, 0, 0],
        [1, 1, 2, 2]
        ]
    assert Solution().findFarmland(land) == expected


def test_2():
    land = [[1, 1], [1, 1]]
    expected = [[0, 0, 1, 1]]
    assert Solution().findFarmland(land) == expected


def test_3():
    land = [[0]]
    expected = []
    assert Solution().findFarmland(land) == expected


def test_4():
    land = [[1, 1, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0]]
    expected = [[0, 5, 0, 5], [0, 0, 1, 1]]
    assert Solution().findFarmland(land) == expected


if __name__ == '__main__':
    # test_1()
    # test_2()
    # test_3()
    test_4()
