#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 100% runtime / 9% mem


class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        tripletsCount = 0
        xors = {0: [0]}
        xor = 0
        for k in range(len(arr)):
            xor ^= arr[k]
            if xor not in xors:
                xors[xor] = [k + 1]
            else:
                for i in xors[xor]:
                    tripletsCount += k - i
                xors[xor].append(k + 1)
        return tripletsCount


def test_1():
    arr = [2, 3, 1, 6, 7]
    expected = 4
    output = Solution().countTriplets(arr)
    assert output == expected


def test_2():
    arr = [1, 1, 1, 1, 1]
    expected = 10
    output = Solution().countTriplets(arr)
    assert output == expected


if __name__ == '__main__':
    test_1()
    test_2()
