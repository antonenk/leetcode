#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 100% runtime / 47% mem


class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        keys = rooms[0]
        rooms[0] = None  # type: ignore
        while len(keys) > 0:
            key = keys.pop()
            if rooms[key] is not None:
                keys += rooms[key]
                rooms[key] = None  # type: ignore

        for room in rooms:
            if room is not None:
                return False
        return True


def test_1():
    assert Solution().canVisitAllRooms([[1], [2], [3], []])


def test_2():
    assert not Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]])


if __name__ == '__main__':
    test_1()
    test_2()
