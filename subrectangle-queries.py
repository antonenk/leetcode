#!/usr/bin/python3

class SubrectangleQueries:

    def __init__(self, rectangle: list[list[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for row in range(row1, row2+1):
            for col in range(col1, col2+1):
                self.rectangle[row][col] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


def test_1():
    subrectangleQueries = SubrectangleQueries([[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]])
# 1 2 1
# 4 3 4
# 3 2 1
# 1 1 1
    assert subrectangleQueries.getValue(0, 2) == 1

    subrectangleQueries.updateSubrectangle(0, 0, 3, 2, 5)
# 5 5 5
# 5 5 5
# 5 5 5
# 5 5 5
    assert subrectangleQueries.getValue(0, 2) == 5
    assert subrectangleQueries.getValue(3, 1) == 5

    subrectangleQueries.updateSubrectangle(3, 0, 3, 2, 10)
# 5   5   5
# 5   5   5
# 5   5   5
# 10  10  10
    assert subrectangleQueries.getValue(3, 1) == 10
    assert subrectangleQueries.getValue(0, 2) == 5


def test_2():
    subrectangleQueries = SubrectangleQueries([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    assert subrectangleQueries.getValue(0, 0) == 1

    subrectangleQueries.updateSubrectangle(0, 0, 2, 2, 100)
    assert subrectangleQueries.getValue(0, 0) == 100
    assert subrectangleQueries.getValue(2, 2) == 100

    subrectangleQueries.updateSubrectangle(1, 1, 2, 2, 20)
    assert subrectangleQueries.getValue(2, 2) == 20


if __name__ == '__main__':
    test_1()
    test_2()
