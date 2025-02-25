#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 100% runtime / 42% mem


class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        cols = len(board[0])
        shipsCount = 0
        for r in range(len(board)):
            isVerticalShip = False
            for c in range(cols):
                if board[r][c] == "X":
                    if not isVerticalShip and (r == 0 or board[r - 1][c] == "."):
                        isVerticalShip = True
                        shipsCount += 1
                else:
                    isVerticalShip = False

        return shipsCount


def test_1():
    board = [
        ["X", "X", ".", "X"],
        [".", ".", ".", "X"],
        [".", ".", ".", "X"]
        ]
    assert Solution().countBattleships(board) == 2


def test_2():
    board = [["."]]
    assert Solution().countBattleships(board) == 0


if __name__ == '__main__':
    test_1()
    test_2()
