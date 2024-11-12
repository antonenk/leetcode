#!/usr/bin/python3

# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/
# beats 69% runtime / 97% mem


class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        groups = []
        groupsBySize = {}
        for i in range(len(groupSizes)):
            size = groupSizes[i]
            if size not in groupsBySize:
                groupsBySize[size] = [i]
            else:
                groupsBySize[size].append(i)

            if len(groupsBySize[size]) == size:
                groups.append(groupsBySize.pop(size))

        return groups


def test_1():
    assert Solution().groupThePeople([3, 3, 3, 3, 3, 1, 3]) == [[0, 1, 2], [5], [3, 4, 6]]


def test_2():
    assert Solution().groupThePeople([2, 1, 3, 3, 3, 2]) == [[1], [2, 3, 4], [0, 5]]


if __name__ == '__main__':
    test_1()
    test_2()
