#!/usr/bin/python3

# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/
# beats 47% runtime / 8% mem


class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        busyBoxes = []
        for boxId in range(len(boxes)):
            if boxes[boxId] == "1":
                busyBoxes.append(boxId)
        result = []
        for boxId in range(len(boxes)):
            result.append(sum([abs(busyBox - boxId) for busyBox in busyBoxes]))

        return result


def test_1():
    assert Solution().minOperations("110") == [1, 1, 3]


def test_2():
    assert Solution().minOperations("001011") == [11, 8, 5, 4, 3, 4]


if __name__ == '__main__':
    test_1()
    test_2()
