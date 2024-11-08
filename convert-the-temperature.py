#!/usr/bin/python3

# https://leetcode.com/problems//description/


class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]


def test_1():
    assert Solution().convertTemperature(36.5) == [309.65, 97.7]


def test_2():
    assert Solution().convertTemperature(122.11) == [395.26, 251.798]


if __name__ == '__main__':
    test_1()
    test_2()
