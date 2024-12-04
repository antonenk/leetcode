#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 100% runtime / 6% mem


class Solution:
    def wateringPlants(self, plants: list[int], capacity: int) -> int:
        steps = 0
        water = capacity
        for position in range(len(plants)):
            if plants[position] <= water:
                steps += 1
                water -= plants[position]
            else:
                steps += 2 * position + 1
                water = capacity - plants[position]
        return steps


def test_1():
    assert Solution().wateringPlants([2, 2, 3, 3], 5) == 14


def test_2():
    assert Solution().wateringPlants([1, 1, 1, 4, 2, 3], 4) == 30


def test_3():
    assert Solution().wateringPlants([7, 7, 7, 7, 7, 7, 7], 8) == 49


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
