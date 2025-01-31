#!/usr/bin/python3

# https://leetcode.com/problems/rotating-the-box/description/
# beats 84% runtime / 26% mem


class Solution:
    def rotateTheBox(self,  boxGrid: list[list[str]]) -> list[list[str]]:
        rows = len(boxGrid)
        cols = len(boxGrid[0])

        rotatedBox = [['.'] * rows for _ in range(cols)]
        for r in range(rows):
            rotatedRow = rows - r - 1
            stones = 0
            for c in range(cols):
                box = boxGrid[r][c]
                if box == "#":
                    stones += 1
                elif box == "*":
                    for c1 in range(c - 1, c - 1 - stones, -1):
                        rotatedBox[c1][rotatedRow] = "#"
                    rotatedBox[c][rotatedRow] = "*"
                    stones = 0

            for c1 in range(cols - 1, cols - 1 - stones, -1):
                rotatedBox[c1][rotatedRow] = "#"

        return rotatedBox


def test_1():
    boxGrid = [["#", ".", "#"]]
    expected = [
        ["."],
        ["#"],
        ["#"]]
    assert Solution().rotateTheBox(boxGrid) == expected


def test_2():
    boxGrid = [
        ["#", ".", "*", "."],
        ["#", "#", "*", "."]]
    expected = [
        ["#", "."],
        ["#", "#"],
        ["*", "*"],
        [".", "."]]
    assert Solution().rotateTheBox(boxGrid) == expected


def test_3():
    boxGrid = [
        ["#", "#", "*", ".", "*", "."],
        ["#", "#", "#", "*", ".", "."],
        ["#", "#", "#", ".", "#", "."]]
    expected = [
        [".", "#", "#"],
        [".", "#", "#"],
        ["#", "#", "*"],
        ["#", "*", "."],
        ["#", ".", "*"],
        ["#", ".", "."]]
    assert Solution().rotateTheBox(boxGrid) == expected


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
