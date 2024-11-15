#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 5% runtime / 18% mem


def spiralCoordinates(rStart, cStart):
    rMin = rMax = rStart
    cMin = cMax = cStart

    yield (rMin, cMin)
    while True:
        for c in range(cMin + 1, cMax + 2):
            yield (rMin, c)
        cMax += 1

        for r in range(rMin + 1, rMax + 2):
            yield (r, cMax)
        rMax += 1

        for c in range(cMax - 1, cMin - 2, -1):
            yield (rMax, c)
        cMin -= 1

        for r in range(rMax - 1, rMin - 2, -1):
            yield (r, cMin)
        rMin -= 1


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        coordinates = []
        gen = spiralCoordinates(rStart, cStart)
        while len(coordinates) < rows * cols:
            r, c = next(gen)
            print(r, ", ", c)
            if r >= 0 and r < rows and c >= 0 and c < cols:
                coordinates.append([r, c])
        return coordinates


def test_1():
    rows = 1
    cols = 4
    rStart = 0
    cStart = 0
    coordinates = [[0, 0], [0, 1], [0, 2], [0, 3]]
    assert Solution().spiralMatrixIII(rows, cols, rStart, cStart) == coordinates


def test_2():
    rows = 5
    cols = 6
    rStart = 1
    cStart = 4
    coordinates = [
        [1,4],[1,5],
        [2,5],
        [2,4],[2,3],
        [1,3],[0,3],
        [0,4],[0,5], # [0,6],
        # [1,6], [2,6], [3,6],
        [3,5],[3,4],[3,3],[3,2],
        [2,2],[1,2],[0,2], # [-1,2]
        # [-1, 3] ... [-1, 
        # []
        [4,5],[4,4],[4,3],[4,2],[4,1],
        [3,1],[2,1],[1,1],[0,1],
        #
        #
        [4,0],[3,0],[2,0],[1,0],[0,0]
        ]
    assert Solution().spiralMatrixIII(rows, cols, rStart, cStart) == coordinates


if __name__ == '__main__':
    test_2()
    test_1()
