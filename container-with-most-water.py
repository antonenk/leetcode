#!/usr/bin/python3

class Solution:
    def maxAreaN2(self, height: list[int]) -> int:
        maxArea = 0
        for i in range(1, len(height)):
            for j in range(i):
                area = min(height[i], height[j]) * (i - j)
                if area > maxArea:
                    maxArea = area
        return maxArea

    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1

        maxArea = 0
        while j > i:
            area = min(height[i], height[j]) * (j - i)
            if area > maxArea:
                maxArea = area

            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return maxArea


def test_1():
    assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_2():
    assert Solution().maxArea([1, 1]) == 1


if __name__ == '__main__':
    test_1()
    test_2()
