#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 34% runtime / 5% mem


class Solution:
    def executeInstructions(self, n: int, startPos: list[int], s: str) -> list[int]:
        result = []
        for start in range(len(s)):
            row = startPos[0]
            col = startPos[1]
            shift = 0
            while start + shift < len(s):
                instruction = s[start + shift]
                if instruction == "L":
                    col -= 1
                elif instruction == "R":
                    col += 1
                elif instruction == "U":
                    row -= 1
                elif instruction == "D":
                    row += 1
                if row == -1 or row == n or col == -1 or col == n:
                    break
                shift += 1
            result.append(shift)
        return result


def test_1():
    assert Solution().executeInstructions(3, [0, 1], "RRDDLU") == [1, 5, 4, 3, 1, 0]


def test_2():
    assert Solution().executeInstructions(2, [1, 1], "LURD") == [4, 1, 0, 0]


if __name__ == '__main__':
    test_1()
    test_2()
