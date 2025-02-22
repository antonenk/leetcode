#!/usr/bin/python3

# https://leetcode.com/problems/sliding-puzzle/description/
# beats 71% runtime / 69% mem


class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        targetState = "".join([str(i) for i in board[0]]) + "".join([str(i) for i in board[1]])
        initState = "123450"
        if targetState == initState:
            return 0
        prevStates = [initState]
        states = set(prevStates)
        move = 1
        while len(prevStates) > 0:
            nextStates = []
            for state in prevStates:
                emptyCell = state.index("0")
                if emptyCell == 0:
                    nextStates.append(state[1] + "0" + state[2:])
                    nextStates.append(state[3] + state[1:3] + "0" + state[4:])
                elif emptyCell == 1:
                    nextStates.append("0" + state[0] + state[2:])
                    nextStates.append(state[0] + state[2] + "0" + state[3:6])
                    nextStates.append(state[0] + state[4] + state[2:4] + "0" + state[5])
                elif emptyCell == 2:
                    nextStates.append(state[0] + "0" + state[1] + state[3:])
                    nextStates.append(state[0:2] + state[5] + state[3:5] + "0")
                elif emptyCell == 3:
                    nextStates.append("0" + state[1:3] + state[0] + state[4:])
                    nextStates.append(state[0:3] + state[4] + "0" + state[5])
                elif emptyCell == 4:
                    nextStates.append(state[0:3] + "0" + state[3] + state[5])
                    nextStates.append(state[0] + "0" + state[2:4] + state[1] + state[5])
                    nextStates.append(state[0:4] + state[5] + "0")
                elif emptyCell == 5:
                    nextStates.append(state[0:4] + "0" + state[4])
                    nextStates.append(state[0:2] + "0" + state[3:5] + state[2])
            prevStates = []
            for state in nextStates:
                if state not in states:
                    if targetState in nextStates:
                        return move
                    else:
                        states.add(state)
                        prevStates.append(state)
            move += 1

        return -1


def test_1():
    board = [
        [1, 2, 3],
        [4, 0, 5]
        ]
    assert Solution().slidingPuzzle(board) == 1


def test_2():
    board = [
        [1, 2, 3],
        [5, 4, 0]
        ]
    assert Solution().slidingPuzzle(board) == -1


def test_3():
    board = [
        [4, 1, 2],
        [5, 0, 3]
        ]
    assert Solution().slidingPuzzle(board) == 5


def test_4():
    board = [
        [3, 2, 4],
        [1, 5, 0]
        ]
    assert Solution().slidingPuzzle(board) == 14


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
